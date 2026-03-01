const { prompt } = require('enquirer');
const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

// Rich-like styling using chalk and custom formatting
const chalk = require('chalk');
const boxen = require('boxen');

// Check if boxen is installed, if not, use simple console.log
let boxenAvailable = true;
try {
  require.resolve('boxen');
} catch (e) {
  boxenAvailable = false;
}

// Simple box function if boxen is not available
function createBox(text, options = {}) {
  if (boxenAvailable) {
    return boxen(text, {
      padding: 1,
      margin: 1,
      borderStyle: 'round',
      borderColor: 'cyan',
      ...options
    });
  }
  const lines = text.split('\n');
  const width = Math.max(...lines.map(l => l.length)) + 4;
  const border = '═'.repeat(width);
  return `╔${border}╗\n${lines.map(l => `║  ${l.padEnd(width - 2)}  ║`).join('\n')}\n╚${border}╝`;
}

// Display banner
function showBanner() {
  const banner = `
${chalk.cyan.bold('╔═══════════════════════════════════════════════════════╗')}
${chalk.cyan.bold('║')}  ${chalk.white.bold('Plume Network Testnet Bot')}                      ${chalk.cyan.bold('║')}
${chalk.cyan.bold('║')}  ${chalk.gray('Automated faucet claims and transaction management')}  ${chalk.cyan.bold('║')}
${chalk.cyan.bold('╚═══════════════════════════════════════════════════════╝')}
  `;
  console.log(banner);
}

// Display menu
function showMenu() {
  const menu = `
${chalk.cyan('┌─────────────────────────────────────────────────┐')}
${chalk.cyan('│')}  ${chalk.white.bold('MAIN MENU')}                                    ${chalk.cyan('│')}
${chalk.cyan('├─────────────────────────────────────────────────┤')}
${chalk.cyan('│')}  ${chalk.green('1.')} ${chalk.white('Install Dependencies')}                        ${chalk.cyan('│')}
${chalk.cyan('│')}  ${chalk.green('2.')} ${chalk.white('Claim ETH from Faucet')}                       ${chalk.cyan('│')}
${chalk.cyan('│')}  ${chalk.green('3.')} ${chalk.white('Claim GOON Tokens from Faucet')}              ${chalk.cyan('│')}
${chalk.cyan('│')}  ${chalk.green('4.')} ${chalk.white('Daily Check-in')}                             ${chalk.cyan('│')}
${chalk.cyan('│')}  ${chalk.green('5.')} ${chalk.white('Auto Mint NFT')}                              ${chalk.cyan('│')}
${chalk.cyan('│')}  ${chalk.green('6.')} ${chalk.white('Auto Stake')}                                 ${chalk.cyan('│')}
${chalk.cyan('│')}  ${chalk.green('7.')} ${chalk.white('Auto Swap')}                                  ${chalk.cyan('│')}
${chalk.cyan('│')}  ${chalk.green('8.')} ${chalk.white('Settings')}                                   ${chalk.cyan('│')}
${chalk.cyan('│')}  ${chalk.green('9.')} ${chalk.white('About')}                                      ${chalk.cyan('│')}
${chalk.cyan('│')}  ${chalk.red('0.')} ${chalk.white('Exit')}                                         ${chalk.cyan('│')}
${chalk.cyan('└─────────────────────────────────────────────────┘')}
  `;
  console.log(menu);
}

// Install dependencies
async function installDependencies() {
  console.log(chalk.yellow('\n📦 Installing dependencies...\n'));
  try {
    execSync('npm install', { stdio: 'inherit' });
    console.log(chalk.green('\n✅ Dependencies installed successfully!\n'));
  } catch (error) {
    console.log(chalk.red('\n❌ Error installing dependencies. Make sure npm is installed.\n'));
  }
  await waitForEnter();
}

// Claim ETH
async function claimETH() {
  console.log(chalk.cyan('\n💰 Claiming ETH from faucet...\n'));
  try {
    execSync('npm run claim-eth', { stdio: 'inherit' });
  } catch (error) {
    console.log(chalk.red('\n❌ Error claiming ETH.\n'));
  }
  await waitForEnter();
}

// Claim GOON
async function claimGOON() {
  console.log(chalk.cyan('\n🪙 Claiming GOON tokens from faucet...\n'));
  try {
    execSync('npm run claim-goon', { stdio: 'inherit' });
  } catch (error) {
    console.log(chalk.red('\n❌ Error claiming GOON tokens.\n'));
  }
  await waitForEnter();
}

// Daily Check-in
async function dailyCheckin() {
  console.log(chalk.cyan('\n📅 Running daily check-in...\n'));
  try {
    execSync('npm run daily-checkin', { stdio: 'inherit' });
  } catch (error) {
    console.log(chalk.red('\n❌ Error running daily check-in.\n'));
  }
  await waitForEnter();
}

// Auto Mint NFT
async function autoMint() {
  console.log(chalk.cyan('\n🎨 Auto minting NFT...\n'));
  try {
    execSync('npm run auto-mint', { stdio: 'inherit' });
  } catch (error) {
    console.log(chalk.red('\n❌ Error auto minting NFT.\n'));
  }
  await waitForEnter();
}

// Auto Stake
async function autoStake() {
  console.log(chalk.cyan('\n🔒 Auto staking...\n'));
  try {
    execSync('npm run auto-stake', { stdio: 'inherit' });
  } catch (error) {
    console.log(chalk.red('\n❌ Error auto staking.\n'));
  }
  await waitForEnter();
}

// Auto Swap
async function autoSwap() {
  console.log(chalk.cyan('\n🔄 Auto swapping...\n'));
  try {
    execSync('npm run auto-swap', { stdio: 'inherit' });
  } catch (error) {
    console.log(chalk.red('\n❌ Error auto swapping.\n'));
  }
  await waitForEnter();
}

// Settings
async function showSettings() {
  console.clear();
  showBanner();
  
  const settingsPath = path.join(__dirname, '.env');
  const privateKeysPath = path.join(__dirname, 'privateKeys.json');
  
  const settings = {
    '.env file exists': fs.existsSync(settingsPath) ? chalk.green('✓ Yes') : chalk.red('✗ No'),
    'privateKeys.json exists': fs.existsSync(privateKeysPath) ? chalk.green('✓ Yes') : chalk.red('✗ No'),
  };
  
  const settingsText = Object.entries(settings)
    .map(([key, value]) => `${chalk.cyan(key.padEnd(25))}: ${value}`)
    .join('\n');
  
  console.log(createBox(`\n${chalk.white.bold('SETTINGS')}\n\n${settingsText}\n`));
  
  const { action } = await prompt({
    type: 'select',
    name: 'action',
    message: 'Choose an action:',
    choices: [
      { name: 'view', message: 'View .env file' },
      { name: 'edit', message: 'Edit .env file' },
      { name: 'view-keys', message: 'View privateKeys.json' },
      { name: 'edit-keys', message: 'Edit privateKeys.json' },
      { name: 'back', message: 'Back to main menu' }
    ]
  });
  
  if (action === 'view') {
    if (fs.existsSync(settingsPath)) {
      console.log(chalk.cyan('\n.env file contents:\n'));
      console.log(fs.readFileSync(settingsPath, 'utf8'));
    } else {
      console.log(chalk.yellow('\n.env file does not exist. Create it from .env.example\n'));
    }
    await waitForEnter();
    return showSettings();
  } else if (action === 'edit') {
    console.log(chalk.yellow('\nPlease edit .env file manually or copy from .env.example\n'));
    await waitForEnter();
    return showSettings();
  } else if (action === 'view-keys') {
    if (fs.existsSync(privateKeysPath)) {
      console.log(chalk.cyan('\nprivateKeys.json contents:\n'));
      const keys = JSON.parse(fs.readFileSync(privateKeysPath, 'utf8'));
      console.log(chalk.gray(`Found ${keys.length} private key(s)\n`));
    } else {
      console.log(chalk.yellow('\nprivateKeys.json does not exist. Create it from privateKeys.json.example\n'));
    }
    await waitForEnter();
    return showSettings();
  } else if (action === 'edit-keys') {
    console.log(chalk.yellow('\nPlease edit privateKeys.json manually or copy from privateKeys.json.example\n'));
    await waitForEnter();
    return showSettings();
  }
}

// About
async function showAbout() {
  console.clear();
  showBanner();
  
  const aboutText = `
${chalk.white.bold('Plume Network Testnet Bot')}

${chalk.cyan('Version:')} 1.0.0
${chalk.cyan('License:')} MIT

${chalk.yellow.bold('Features:')}
  • Claim ETH and GOON tokens from Plume testnet faucet
  • Automatically handles transactions and errors
  • Provides real-time feedback and transaction details
  • Daily check-in functionality
  • Auto mint NFT
  • Auto stake
  • Auto swap

${chalk.yellow.bold('Requirements:')}
  • Node.js
  • npm or yarn for package management
  • .env file for storing sensitive information
  • privateKeys.json for daily check-ins

${chalk.yellow.bold('Repository:')}
  https://github.com/frankrichardhall/PlumeNetwork-Testnet-bot.git
  `;
  
  console.log(createBox(aboutText));
  await waitForEnter();
}

// Wait for Enter key
function waitForEnter() {
  return new Promise((resolve) => {
    const readline = require('readline');
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });
    
    rl.question(chalk.gray('\nPress Enter to continue...'), () => {
      rl.close();
      resolve();
    });
  });
}

// Main function
async function main() {
  while (true) {
    console.clear();
    showBanner();
    showMenu();
    
    try {
      const { choice } = await prompt({
        type: 'select',
        name: 'choice',
        message: chalk.cyan.bold('Select an option:'),
        choices: [
          { name: '1', message: `${chalk.green('1.')} ${chalk.white('Install Dependencies')}` },
          { name: '2', message: `${chalk.green('2.')} ${chalk.white('Claim ETH from Faucet')}` },
          { name: '3', message: `${chalk.green('3.')} ${chalk.white('Claim GOON Tokens from Faucet')}` },
          { name: '4', message: `${chalk.green('4.')} ${chalk.white('Daily Check-in')}` },
          { name: '5', message: `${chalk.green('5.')} ${chalk.white('Auto Mint NFT')}` },
          { name: '6', message: `${chalk.green('6.')} ${chalk.white('Auto Stake')}` },
          { name: '7', message: `${chalk.green('7.')} ${chalk.white('Auto Swap')}` },
          { name: '8', message: `${chalk.green('8.')} ${chalk.white('Settings')}` },
          { name: '9', message: `${chalk.green('9.')} ${chalk.white('About')}` },
          { name: '0', message: `${chalk.red('0.')} ${chalk.white('Exit')}` }
        ]
      });
      
      const choiceNum = parseInt(choice);
      
      switch (choiceNum) {
        case 1:
          await installDependencies();
          break;
        case 2:
          await claimETH();
          break;
        case 3:
          await claimGOON();
          break;
        case 4:
          await dailyCheckin();
          break;
        case 5:
          await autoMint();
          break;
        case 6:
          await autoStake();
          break;
        case 7:
          await autoSwap();
          break;
        case 8:
          await showSettings();
          break;
        case 9:
          await showAbout();
          break;
        case 0:
          console.log(chalk.yellow('\n👋 Goodbye!\n'));
          process.exit(0);
          break;
      }
    } catch (error) {
      if (error.name === 'ExitPrompt' || error.message === 'User cancelled') {
        console.log(chalk.yellow('\n👋 Goodbye!\n'));
        process.exit(0);
      }
      console.log(chalk.red('\n❌ An error occurred:', error.message));
      await waitForEnter();
    }
  }
}

// Run main function
main().catch(console.error);
