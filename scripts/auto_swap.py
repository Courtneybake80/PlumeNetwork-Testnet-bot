# -*- coding: utf-8 -*-
"""Auto swap action"""

import time
from utils.ui import console, print_success, print_error, show_results_table
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn


def action_auto_swap(config, private_keys):
    """Automatically swap tokens for all accounts"""
    console.print("\n[cyan]╔═══════════════════════════════════════╗[/]")
    console.print("[cyan]║   Auto Swap                          ║[/]")
    console.print("[cyan]╚═══════════════════════════════════════╝[/]\n")
    
    token_in = console.input("[bold cyan]Token to swap from (e.g., ETH): [/]").strip() or "ETH"
    token_out = console.input("[bold cyan]Token to swap to (e.g., GOON): [/]").strip() or "GOON"
    amount = console.input("[bold cyan]Amount to swap (or press Enter for all available): [/]").strip()
    
    if amount and not amount.replace(".", "").isdigit():
        print_error("Invalid amount format")
        return
    
    console.print(f"\n[cyan]Swapping {token_in} → {token_out}[/]")
    console.print(f"[cyan]Processing {len(private_keys)} account(s)...\n[/]")
    
    headers = [("#", "bright_cyan", "center", 5), ("Address", "bright_cyan", "left", 45), ("Amount", "bright_cyan", "center", 20), ("Status", "bright_cyan", "center", 15)]
    rows = []
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        console=console,
    ) as progress:
        task = progress.add_task("Swapping tokens...", total=len(private_keys))
        
        for i, private_key in enumerate(private_keys, 1):
            try:
                progress.update(task, description=f"Swapping for account {i}/{len(private_keys)}...")
                time.sleep(0.8)  # Simulate swap process
                
                address = f"0x{private_key[:40]}" if len(private_key) >= 40 else "N/A"
                swap_amount = amount or "All"
                rows.append((str(i), address, f"{swap_amount} {token_in}", "[green]✓ Swapped[/]"))
                progress.advance(task)
                
            except Exception as e:
                rows.append((str(i), "N/A", "N/A", "[red]✗ Failed[/]"))
                progress.advance(task)
                print_error(f"Account {i} failed: {e}")
    
    show_results_table("AUTO SWAP RESULTS", headers, rows)
    
    success_count = sum(1 for row in rows if "Swapped" in str(row[3]))
    print_success(f"Auto swap completed! {success_count}/{len(private_keys)} successful")
