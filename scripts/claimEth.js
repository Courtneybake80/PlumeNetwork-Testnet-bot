require('dotenv').config();
const { ethers } = require('ethers');
const axios = require('axios');
const chalk = require('chalk');
const ora = require('ora');

const RPC_URL = process.env.RPC_URL || 'https://phoenix-rpc.plumenetwork.xyz';
const FAUCET_URL = process.env.FAUCET_URL || 'https://faucet.plumenetwork.xyz';

async function claimETH() {
  console.log(chalk.cyan.bold('\n╔═══════════════════════════════════════╗'));
  console.log(chalk.cyan.bold('║   Claim ETH from Faucet              ║'));
  console.log(chalk.cyan.bold('╚═══════════════════════════════════════╝\n'));

  const spinner = ora('Initializing...').start();

  try {
    // Get wallet address
    const { prompt } = require('enquirer');
    const { address } = await prompt({
      type: 'input',
      name: 'address',
      message: 'Enter your wallet address:',
      validate: (value) => {
        if (!ethers.isAddress(value)) {
          return 'Please enter a valid Ethereum address';
        }
        return true;
      }
    });

    spinner.text = 'Claiming ETH from faucet...';
    spinner.start();

    // Claim ETH from faucet
    const response = await axios.post(`${FAUCET_URL}/eth`, {
      address: address
    });

    spinner.succeed(chalk.green('ETH claimed successfully!'));
    
    console.log(chalk.green('\n✅ Transaction Details:'));
    console.log(chalk.cyan(`   Address: ${address}`));
    console.log(chalk.cyan(`   Status: ${response.data.status || 'Success'}`));
    if (response.data.txHash) {
      console.log(chalk.cyan(`   Transaction Hash: ${response.data.txHash}`));
    }

  } catch (error) {
    spinner.fail(chalk.red('Failed to claim ETH'));
    console.log(chalk.red(`\n❌ Error: ${error.message}`));
    if (error.response) {
      console.log(chalk.red(`   Status: ${error.response.status}`));
      console.log(chalk.red(`   Message: ${error.response.data?.message || 'Unknown error'}`));
    }
  }
}

claimETH().catch(console.error);
