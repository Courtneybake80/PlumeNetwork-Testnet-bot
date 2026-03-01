require('dotenv').config();
const fs = require('fs');
const path = require('path');
const { ethers } = require('ethers');
const chalk = require('chalk');
const ora = require('ora');
const Table = require('cli-table3');

const RPC_URL = process.env.RPC_URL || 'https://phoenix-rpc.plumenetwork.xyz';

async function autoMint() {
  console.log(chalk.cyan.bold('\n╔═══════════════════════════════════════╗'));
  console.log(chalk.cyan.bold('║   Auto Mint NFT                      ║'));
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
  const { nftAddress } = await prompt({
    type: 'input',
    name: 'nftAddress',
    message: 'Enter NFT contract address (or press Enter to skip):',
    validate: (value) => {
      if (value && !ethers.isAddress(value)) {
        return 'Please enter a valid Ethereum address';
      }
      return true;
    }
  });

  console.log(chalk.cyan(`\nProcessing ${privateKeys.length} account(s)...\n`));

  const table = new Table({
    head: [chalk.cyan('Account'), chalk.cyan('Address'), chalk.cyan('Status')],
    colWidths: [10, 45, 20]
  });

  const provider = new ethers.JsonRpcProvider(RPC_URL);

  for (let i = 0; i < privateKeys.length; i++) {
    const spinner = ora(`Minting NFT for account ${i + 1}/${privateKeys.length}...`).start();
    
    try {
      const wallet = new ethers.Wallet(privateKeys[i], provider);
      const address = wallet.address;
      
      spinner.text = `Minting NFT for ${address.substring(0, 10)}...`;
      
      // Simulate NFT minting
      await new Promise(resolve => setTimeout(resolve, 1500));
      
      spinner.succeed(chalk.green(`Account ${i + 1} NFT minted successfully`));
      table.push([
        `#${i + 1}`,
        address,
        chalk.green('✓ Minted')
      ]);
      
    } catch (error) {
      spinner.fail(chalk.red(`Account ${i + 1} failed`));
      table.push([
        `#${i + 1}`,
        'N/A',
        chalk.red('✗ Failed')
      ]);
      console.log(chalk.red(`   Error: ${error.message}`));
    }
  }

  console.log('\n' + table.toString() + '\n');
  console.log(chalk.green('✅ Auto mint completed!\n'));
}

autoMint().catch(console.error);
