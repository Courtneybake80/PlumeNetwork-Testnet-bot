# -*- coding: utf-8 -*-
"""
Plume Network Testnet Bot
Bot to interact with Plume Network Testnet faucets and manage transactions automatically.
"""

import sys
import os

from utils import ensure_env

# Initialize colorama for Windows
if sys.platform == "win32":
    try:
        import colorama
        colorama.init()
    except ImportError:
        pass

from utils.ui import (
    print_banner,
    print_info,
    print_error,
    show_menu_table,
    console,
    input_pause,
)
from config import load_config, load_private_keys
from scripts.claim_eth import action_claim_eth
from scripts.claim_goon import action_claim_goon
from scripts.daily_checkin import action_daily_checkin
from scripts.auto_mint import action_auto_mint
from scripts.auto_stake import action_auto_stake
from scripts.auto_swap import action_auto_swap
from actions.install import action_install_dependencies
from actions.settings import action_settings
from actions.about import action_about


MENU_ITEMS = [
    ("1", "Install Dependencies", "pip install -r requirements.txt"),
    ("2", "Claim ETH from Faucet", "Claim ETH tokens from the testnet faucet"),
    ("3", "Claim GOON Tokens", "Claim GOON tokens from the testnet faucet"),
    ("4", "Daily Check-in", "Perform daily check-in for all accounts"),
    ("5", "Auto Mint NFT", "Automatically mint NFTs"),
    ("6", "Auto Stake", "Automatically stake tokens"),
    ("7", "Auto Swap", "Automatically swap tokens"),
    ("8", "Settings", "View and edit configuration files"),
    ("9", "About", "Show information about the bot"),
    ("0", "Exit", "Quit the application"),
]


@ensure_env
def main():
    """Main entry point for the Plume Network Testnet Bot"""
    print_banner()
    
    # Load configuration
    config = load_config()
    private_keys = load_private_keys()
    
    # Show status if keys are loaded
    if private_keys:
        console.print(f"\n[cyan]✓[/] Loaded [bold]{len(private_keys)}[/] account(s) from privateKeys.json\n")
    else:
        console.print("\n[yellow]![/] No private keys found. Add keys to [bold]privateKeys.json[/]\n")
    
    while True:
        choice = show_menu_table(MENU_ITEMS)
        
        if choice == "0":
            print_info("Goodbye!")
            sys.exit(0)
        elif choice == "1":
            action_install_dependencies()
        elif choice == "2":
            action_claim_eth(config)
        elif choice == "3":
            action_claim_goon(config)
        elif choice == "4":
            if not private_keys:
                print_error("No private keys found. Add keys to privateKeys.json")
            else:
                action_daily_checkin(config, private_keys)
        elif choice == "5":
            if not private_keys:
                print_error("No private keys found. Add keys to privateKeys.json")
            else:
                action_auto_mint(config, private_keys)
        elif choice == "6":
            if not private_keys:
                print_error("No private keys found. Add keys to privateKeys.json")
            else:
                action_auto_stake(config, private_keys)
        elif choice == "7":
            if not private_keys:
                print_error("No private keys found. Add keys to privateKeys.json")
            else:
                action_auto_swap(config, private_keys)
        elif choice == "8":
            action_settings()
        elif choice == "9":
            action_about()
        else:
            print_error("Invalid choice. Enter 0-9.")
        
        # Refresh loaded data in case user edited files between runs
        private_keys = load_private_keys()
        input_pause()


if __name__ == "__main__":
    main()
