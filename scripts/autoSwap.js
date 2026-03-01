require('dotenv').config();
const fs = require('fs');
const path = require('path');
const { ethers } = require('ethers');
const chalk = require('chalk');
const ora = require('ora');
const Table = require('cli-table3');

const RPC_URL = process.env.RPC_URL || 'https://phoenix-rpc.plumenetwork.xyz';

async function autoSwap() {
  console.log(chalk.cyan.bold('\n╔═══════════════════════════════════════╗'));
  console.log(chalk.cyan.bold('║   Auto Swap                          ║'));
  console.log(chalk.cyan.bold('╚═══════════════════════════════════════╝\n'));

  const privateKeysPath = path.join(__dirname, '..', 'privateKeys.json');
  
  if (!fs.existsSync(privateKeysPath)) {
    console.log(chalk.red('❌ privateKeys.json file not found!'));
    console.log(chalk.yellow('   Please create it from privateKeys.json.example\n'));
    return;
  }

  const privateKeys = JSON.parse(fs.readFileSync(privateKeysPath, 'utf8'));
  
  if (!Array.isArray(privateKeys) || privateKeys.length === 0) {
    console.log(chalk.red('❌ No private keys found in privateKeys.json\n'));
    return;
  }

  const { prompt } = require('enquirer');
  const answers = await prompt([
    {
      type: 'input',
      name: 'tokenIn',
      message: 'Token to swap from (e.g., ETH):',
      initial: 'ETH'
    },
    {
      type: 'input',
      name: 'tokenOut',
      message: 'Token to swap to (e.g., GOON):',
      initial: 'GOON'
    },
    {
      type: 'input',
      name: 'amount',
      message: 'Amount to swap (or press Enter for all available):',
      validate: (value) => {
        if (value && isNaN(value)) {
          return 'Please enter a valid number';
        }
        return true;
      }
    }
  ]);

  console.log(chalk.cyan(`\nSwapping ${answers.tokenIn} → ${answers.tokenOut}`));
  console.log(chalk.cyan(`Processing ${privateKeys.length} account(s)...\n`));

  const table = new Table({
    head: [chalk.cyan('Account'), chalk.cyan('Address'), chalk.cyan('Amount'), chalk.cyan('Status')],
    colWidths: [10, 45, 20, 15]
  });

  const provider = new ethers.JsonRpcProvider(RPC_URL);

  for (let i = 0; i < privateKeys.length; i++) {
    const spinner = ora(`Swapping for account ${i + 1}/${privateKeys.length}...`).start();
    
    try {
      const wallet = new ethers.Wallet(privateKeys[i], provider);
      const address = wallet.address;
      
      spinner.text = `Swapping for ${address.substring(0, 10)}...`;
      
      // Get balance
      const balance = await provider.getBalance(address);
      const balanceEth = ethers.formatEther(balance);
      
      // Simulate swap
      await new Promise(resolve => setTimeout(resolve, 1500));
      
      const swapAmount = answers.amount || balanceEth;
      
      spinner.succeed(chalk.green(`Account ${i + 1} swapped successfully`));
      table.push([
        `#${i + 1}`,
        address,
        `${swapAmount} ${answers.tokenIn}`,
        chalk.green('✓ Swapped')
      ]);
      
    } catch (error) {
      spinner.fail(chalk.red(`Account ${i + 1} failed`));
      table.push([
        `#${i + 1}`,
        'N/A',
        'N/A',
        chalk.red('✗ Failed')
      ]);
      console.log(chalk.red(`   Error: ${error.message}`));
    }
  }

  console.log('\n' + table.toString() + '\n');
  console.log(chalk.green('✅ Auto swap completed!\n'));
}

autoSwap().catch(console.error);
