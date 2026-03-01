# PlumeNetwork-Testnet-bot
Plume Network Testnet Bot — Automated faucet claims, daily check-ins, NFT minting, staking, and token swaps for Plume Network RWAfi testnet with multi-account management, Node.js integration, proxy support, and Rich CLI for real-world asset tokenization platform farming
<div align="center">

```
██████╗ ██╗     ██╗   ██╗███╗   ███╗███████╗    ███╗   ██╗███████╗████████╗██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗
██╔══██╗██║     ██║   ██║████╗ ████║██╔════╝    ████╗  ██║██╔════╝╚══██╔══╝██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝
██████╔╝██║     ██║   ██║██╔████╔██║█████╗      ██╔██╗ ██║█████╗     ██║   ██║ █╗ ██║██║   ██║██████╔╝█████╔╝ 
██╔═══╝ ██║     ██║   ██║██║╚██╔╝██║██╔══╝      ██║╚██╗██║██╔══╝     ██║   ██║███╗██║██║   ██║██╔══██╗██╔═██╗ 
██║     ███████╗╚██████╔╝██║ ╚═╝ ██║███████╗    ██║ ╚████║███████╗   ██║   ╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗
╚═╝     ╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝    ╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
                        TESTNET BOT
```

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Node.js](https://img.shields.io/badge/Node.js-18+-339933?style=for-the-badge&logo=node.js&logoColor=white)](https://nodejs.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Plume](https://img.shields.io/badge/Plume-Network-8B5CF6?style=for-the-badge)](https://plumenetwork.xyz/)

**Automated faucet claims, daily check-ins, NFT minting, staking, and swaps for the Plume Network Testnet.**

[Features](#-features) · [Getting Started](#-getting-started) · [Configuration](#-configuration) · [Usage](#-usage) · [FAQ](#-faq)

</div>

---

## Registration & Official Links

| # | Resource | URL |
|:-:|----------|-----|
| 1 | Plume Network Official | https://plumenetwork.xyz/ |
| 2 | Plume Testnet Portal | https://deform.plumenetwork.xyz/testnet/ |
| 3 | Plume Testnet Faucet | https://faucet.plumenetwork.xyz/ |
| 4 | Plume RPC Endpoint | https://phoenix-rpc.plumenetwork.xyz |
| 5 | Plume Documentation | https://docs.plumenetwork.xyz/ |
| 6 | Plume Blog | https://plume.org/blog |

> Plume Network is a purpose-built EVM-compatible blockchain for Real-World Asset finance (RWAfi). It bridges traditional finance and DeFi by tokenizing assets like private credit, real estate, and commodities. Plume launched mainnet in Q3 2025, reaching $645M+ in RWA TVL and becoming the #1 chain for RWA holders globally.

---

## Features

<table>
<tr><td>

### Faucet & Rewards
| Status | Feature |
|:------:|---------|
| ✅ | Claim ETH from testnet faucet |
| ✅ | Claim GOON tokens from faucet |
| ✅ | Daily check-in for all accounts |
| ✅ | Real-time transaction feedback |

</td><td>

### DeFi Automation
| Status | Feature |
|:------:|---------|
| ✅ | Auto Mint NFT |
| ✅ | Auto Stake tokens |
| ✅ | Auto Swap tokens |
| ✅ | Automatic error handling & retries |

</td></tr>
<tr><td>

### Multi-Runtime
| Status | Feature |
|:------:|---------|
| ✅ | Python version (main.py) |
| ✅ | Node.js version (index.js) |
| ✅ | Shared config format |
| ✅ | One-click launchers (run.bat / run.sh) |

</td><td>

### Account Management
| Status | Feature |
|:------:|---------|
| ✅ | Multi-account via privateKeys.json |
| ✅ | .env-based configuration |
| ✅ | Built-in settings editor |
| ✅ | Account key hot-reload between runs |

</td></tr>
</table>

---

## Getting Started

### Prerequisites

| Requirement | Version | Notes |
|-------------|---------|-------|
| Python | 3.8+ | For the Python version |
| Node.js | 18+ | For the Node.js version |
| pip | latest | Python package manager |
| npm | latest | Node.js package manager (ships with Node) |

### Installation — Windows (One-Click)

```bash
git clone https://github.com/shellgainer/PlumeNetwork-Testnet-bot.git
cd PlumeNetwork-Testnet-bot
run.bat
```

### Installation — Manual (Python)

```bash
git clone https://github.com/shellgainer/PlumeNetwork-Testnet-bot.git
cd PlumeNetwork-Testnet-bot
pip install -r requirements.txt
copy .env.example .env
copy privateKeys.json.example privateKeys.json
python main.py
```

### Installation — Manual (Node.js)

```bash
git clone https://github.com/shellgainer/PlumeNetwork-Testnet-bot.git
cd PlumeNetwork-Testnet-bot
npm install
copy .env.example .env
copy privateKeys.json.example privateKeys.json
node index.js
```

### Python Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| rich | ≥13.7.0 | Terminal UI (panels, tables, menus) |
| python-dotenv | ≥1.0.0 | .env file loader |
| requests | ≥2.31.0 | HTTP requests to faucet APIs |
| colorama | ≥0.4.6 | Cross-platform terminal colors |

### Node.js Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| ethers | ^6.9.0 | Blockchain interaction & signing |
| axios | ^1.6.2 | HTTP requests |
| dotenv | ^16.3.1 | .env file loader |
| chalk | ^4.1.2 | Terminal colors |
| enquirer | ^2.4.1 | Interactive CLI prompts |
| ora | ^5.4.1 | Spinner animations |
| cli-table3 | ^0.6.5 | Table rendering |

---

## Configuration

### `.env` — Network Configuration

```env
# Plume Network Testnet Configuration
RPC_URL=https://phoenix-rpc.plumenetwork.xyz
FAUCET_URL=https://faucet.plumenetwork.xyz
CHAIN_ID=161221135

# Optional: API key for rate-limited endpoints
# API_KEY=your_api_key_here
```

### `privateKeys.json` — Wallet Private Keys

```json
[
  "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2",
  "f6e5d4c3b2a1f6e5d4c3b2a1f6e5d4c3b2a1f6e5d4c3b2a1f6e5d4c3b2a1f6e5",
  "1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"
]
```

---

## Usage

### Python Version

```bash
python main.py
```

### Node.js Version

```bash
node index.js
# or
npm start
```

### Menu Options

```
┌────────────────────────────────────────────────────────────┐
│           PLUME NETWORK TESTNET BOT MENU                   │
├─────┬────────────────────────┬─────────────────────────────┤
│  #  │ Action                 │ Description                 │
├─────┼────────────────────────┼─────────────────────────────┤
│  1  │ Install Dependencies   │ pip install -r requirements │
│  2  │ Claim ETH from Faucet  │ Claim testnet ETH tokens    │
│  3  │ Claim GOON Tokens      │ Claim testnet GOON tokens   │
│  4  │ Daily Check-in         │ Check-in for all accounts   │
│  5  │ Auto Mint NFT          │ Automatically mint NFTs     │
│  6  │ Auto Stake             │ Automatically stake tokens  │
│  7  │ Auto Swap              │ Automatically swap tokens   │
│  8  │ Settings               │ Edit config files           │
│  9  │ About                  │ Project information         │
│  0  │ Exit                   │ Quit the application        │
└─────┴────────────────────────┴─────────────────────────────┘
```

### Node.js Script Shortcuts

| Command | Action |
|---------|--------|
| `npm run claim-eth` | Claim ETH from faucet |
| `npm run claim-goon` | Claim GOON tokens |
| `npm run daily-checkin` | Daily check-in |
| `npm run auto-mint` | Auto mint NFTs |
| `npm run auto-stake` | Auto stake tokens |
| `npm run auto-swap` | Auto swap tokens |

---

## Project Structure

```
PlumeNetwork-Testnet-bot/
├── main.py                     # Python entry point (Rich TUI menu)
├── index.js                    # Node.js entry point
├── config.py                   # Python config loader (.env + privateKeys)
├── requirements.txt            # Python dependencies
├── package.json                # Node.js dependencies & scripts
├── .env.example                # Environment config template
├── privateKeys.json.example    # Private keys template
├── run.bat                     # Windows one-click launcher
├── run.sh                      # Linux/macOS one-click launcher
├── scripts/
│   ├── claim_eth.py            # [PY] ETH faucet claim
│   ├── claim_goon.py           # [PY] GOON token faucet claim
│   ├── daily_checkin.py        # [PY] Daily check-in automation
│   ├── auto_mint.py            # [PY] NFT minting automation
│   ├── auto_stake.py           # [PY] Token staking automation
│   ├── auto_swap.py            # [PY] Token swap automation
│   ├── claimEth.js             # [JS] ETH faucet claim
│   ├── claimGoon.js            # [JS] GOON token faucet claim
│   ├── dailyCheckin.js         # [JS] Daily check-in
│   ├── autoMint.js             # [JS] NFT minting
│   ├── autoStake.js            # [JS] Token staking
│   └── autoSwap.js             # [JS] Token swap
├── actions/
│   ├── install.py              # Dependency installer action
│   ├── settings.py             # Settings editor action
│   └── about.py                # About screen
└── utils/
    └── ui.py                   # Rich TUI utilities (banner, tables, helpers)
```

---

## FAQ

<details>
<summary><b>Should I use the Python or Node.js version?</b></summary>

Both versions offer the same functionality. The Python version provides a Rich TUI interface with panels and tables. The Node.js version uses chalk/enquirer for a similar experience. Pick whichever runtime you're more comfortable with.
</details>

<details>
<summary><b>How do I add multiple accounts?</b></summary>

Add all private keys to `privateKeys.json` as an array of hex strings. Each account will be processed sequentially for faucet claims, check-ins, minting, staking, and swaps.
</details>

<details>
<summary><b>What is the GOON token?</b></summary>

GOON is a testnet token on the Plume Network used for testing DeFi interactions. It can be claimed from the faucet alongside testnet ETH. It has no real monetary value.
</details>

<details>
<summary><b>How often can I claim from the faucet?</b></summary>

Faucet claim limits are set by the Plume Network and may change. Typically there is a cooldown period per wallet address. The bot handles rate limiting and will report when claims are available.
</details>

<details>
<summary><b>Is this safe for mainnet?</b></summary>

**No.** This bot is designed exclusively for the Plume Network Testnet. Never use mainnet private keys or wallets with real funds. Always use burner wallets.
</details>

<details>
<summary><b>What if the faucet returns an error?</b></summary>

The bot includes automatic error handling and will display the specific error message. Common issues: cooldown not expired, faucet rate limit reached, or network connectivity problems. Wait and retry.
</details>

---

## Disclaimer

> This software is provided for **educational and testnet purposes only**. It is designed to interact with the Plume Network Testnet and should never be used with mainnet wallets containing real assets. Use burner wallets exclusively. Never share your private keys. The developers assume no liability for any loss or damage resulting from the use of this tool. Always review the source code before running. By using this software you accept full responsibility for your actions.

---

<div align="center">

If this project helped you, consider giving it a star!

[![Star](https://img.shields.io/github/stars/shellgainer/PlumeNetwork-Testnet-bot?style=for-the-badge&color=yellow)](https://github.com/shellgainer/PlumeNetwork-Testnet-bot)

MIT License

</div>
