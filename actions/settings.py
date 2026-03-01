# -*- coding: utf-8 -*-
"""Settings action"""

import os
from pathlib import Path
from utils.ui import (
    console,
    print_info,
    print_error,
    print_warning,
    show_simple_list,
    show_results_table,
    input_pause,
)
from config import load_config, load_private_keys


def action_settings():
    """Show and manage settings"""
    console.clear()
    
    config = load_config()
    private_keys = load_private_keys()
    
    env_path = Path(".env")
    keys_path = Path("privateKeys.json")
    
    # Show settings status
    headers = [("Setting", "bright_cyan", "left", 30), ("Status", "bright_cyan", "center", 20), ("Value", "grey58", "left", 40)]
    rows = [
        (".env file", "[green]✓ Exists[/]" if env_path.exists() else "[red]✗ Missing[/]", 
         "See .env.example" if not env_path.exists() else "Configured"),
        ("privateKeys.json", "[green]✓ Exists[/]" if keys_path.exists() else "[red]✗ Missing[/]",
         f"{len(private_keys)} key(s)" if keys_path.exists() else "See privateKeys.json.example"),
        ("RPC URL", "[green]✓[/]", config.get("RPC_URL", "N/A")),
        ("Faucet URL", "[green]✓[/]", config.get("FAUCET_URL", "N/A")),
        ("Chain ID", "[green]✓[/]", str(config.get("CHAIN_ID", "N/A"))),
    ]
    
    show_results_table("SETTINGS", headers, rows)
    
    # Show menu
    console.print("[bold cyan]Options:[/]")
    console.print("  [cyan]1[/] View .env file")
    console.print("  [cyan]2[/] View privateKeys.json")
    console.print("  [cyan]3[/] Back to main menu")
    
    choice = console.input("\n[bold cyan]Select option: [/]").strip()
    
    if choice == "1":
        if env_path.exists():
            console.print("\n[cyan].env file contents:[/]\n")
            with open(env_path, "r", encoding="utf-8") as f:
                console.print(f"[dim]{f.read()}[/]")
        else:
            print_warning(".env file does not exist. Create it from .env.example")
        input_pause()
        action_settings()
    elif choice == "2":
        if keys_path.exists():
            console.print(f"\n[cyan]Found {len(private_keys)} private key(s)[/]\n")
            print_warning("Private keys are hidden for security reasons.")
            console.print("Edit privateKeys.json manually to add/remove keys.")
        else:
            print_warning("privateKeys.json does not exist. Create it from privateKeys.json.example")
        input_pause()
        action_settings()
    elif choice == "3":
        return
    else:
        print_error("Invalid choice")
        input_pause()
        action_settings()
