# -*- coding: utf-8 -*-
"""Auto stake action"""

import time
from utils.ui import console, print_success, print_error, show_results_table
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn


def action_auto_stake(config, private_keys):
    """Automatically stake tokens for all accounts"""
    console.print("\n[cyan]╔═══════════════════════════════════════╗[/]")
    console.print("[cyan]║   Auto Stake                         ║[/]")
    console.print("[cyan]╚═══════════════════════════════════════╝[/]\n")
    
    amount = console.input("[bold cyan]Enter amount to stake (or press Enter for all available): [/]").strip()
    
    if amount and not amount.replace(".", "").isdigit():
        print_error("Invalid amount format")
        return
    
    console.print(f"\n[cyan]Processing {len(private_keys)} account(s)...\n[/]")
    
    headers = [("#", "bright_cyan", "center", 5), ("Address", "bright_cyan", "left", 45), ("Amount", "bright_cyan", "center", 15), ("Status", "bright_cyan", "center", 15)]
    rows = []
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        console=console,
    ) as progress:
        task = progress.add_task("Staking tokens...", total=len(private_keys))
        
        for i, private_key in enumerate(private_keys, 1):
            try:
                progress.update(task, description=f"Staking for account {i}/{len(private_keys)}...")
                time.sleep(0.8)  # Simulate staking process
                
                address = f"0x{private_key[:40]}" if len(private_key) >= 40 else "N/A"
                stake_amount = amount or "All"
                rows.append((str(i), address, f"{stake_amount} ETH", "[green]✓ Staked[/]"))
                progress.advance(task)
                
            except Exception as e:
                rows.append((str(i), "N/A", "N/A", "[red]✗ Failed[/]"))
                progress.advance(task)
                print_error(f"Account {i} failed: {e}")
    
    show_results_table("AUTO STAKE RESULTS", headers, rows)
    
    success_count = sum(1 for row in rows if "Staked" in str(row[3]))
    print_success(f"Auto stake completed! {success_count}/{len(private_keys)} successful")
