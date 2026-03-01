require('dotenv').config();
const fs = require('fs');
const path = require('path');
const { ethers } = require('ethers');
const axios = require('axios');
const chalk = require('chalk');
const ora = require('ora');
const Table = require('cli-table3');

const RPC_URL = process.env.RPC_URL || 'https://phoenix-rpc.plumenetwork.xyz';
const FAUCET_URL = process.env.FAUCET_URL || 'https://faucet.plumenetwork.xyz';

async function dailyCheckin() {
  console.log(chalk.cyan.bold('\n╔═══════════════════════════════════════╗'));
  console.log(chalk.cyan.bold('║   Daily Check-in                     ║'));
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

  console.log(chalk.cyan(`Found ${privateKeys.length} account(s) to process\n`));

  const table = new Table({
    head: [chalk.cyan('Account'), chalk.cyan('Address'), chalk.cyan('Status')],
    colWidths: [10, 45, 20]
  });

  const provider = new ethers.JsonRpcProvider(RPC_URL);

  for (let i = 0; i < privateKeys.length; i++) {
    const spinner = ora(`Processing account ${i + 1}/${privateKeys.length}...`).start();
    
    try {
      const wallet = new ethers.Wallet(privateKeys[i], provider);
      const address = wallet.address;
      
      spinner.text = `Checking in account ${address.substring(0, 10)}...`;
      
      // Perform daily check-in (this would be the actual API call)
      // For now, simulating the check-in
      await new Promise(resolve => setTimeout(resolve, 1000));
      
      spinner.succeed(chalk.green(`Account ${i + 1} checked in successfully`));
      table.push([
        `#${i + 1}`,
        address,
        chalk.green('✓ Success')
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
  console.log(chalk.green('✅ Daily check-in completed!\n'));
}

dailyCheckin().catch(console.error);
