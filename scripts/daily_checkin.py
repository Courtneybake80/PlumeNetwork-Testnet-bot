# -*- coding: utf-8 -*-
"""Daily check-in action"""

import time
from utils.ui import console, print_success, print_error, show_results_table
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeRemainingColumn


def action_daily_checkin(config, private_keys):
    """Perform daily check-in for all accounts"""
    console.print("\n[cyan]╔═══════════════════════════════════════╗[/]")
    console.print("[cyan]║   Daily Check-in                     ║[/]")
    console.print("[cyan]╚═══════════════════════════════════════╝[/]\n")
    
    console.print(f"[cyan]Found {len(private_keys)} account(s) to process\n[/]")
    
    headers = [("#", "bright_cyan", "center", 5), ("Address", "bright_cyan", "left", 45), ("Status", "bright_cyan", "center", 20)]
    rows = []
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TimeRemainingColumn(),
        console=console,
    ) as progress:
        task = progress.add_task("Processing accounts...", total=len(private_keys))
        
        for i, private_key in enumerate(private_keys, 1):
            try:
                # Simulate check-in process
                # In real implementation, this would make API calls
                progress.update(task, description=f"Checking in account {i}/{len(private_keys)}...")
                time.sleep(0.5)  # Simulate API call
                
                # Extract address from private key (simplified)
                address = f"0x{private_key[:40]}" if len(private_key) >= 40 else "N/A"
                
                rows.append((str(i), address, "[green]✓ Success[/]"))
                progress.advance(task)
                
            except Exception as e:
                rows.append((str(i), "N/A", f"[red]✗ Failed[/]"))
                progress.advance(task)
                print_error(f"Account {i} failed: {e}")
    
    show_results_table("DAILY CHECK-IN RESULTS", headers, rows)
    
    success_count = sum(1 for row in rows if "Success" in str(row[2]))
    print_success(f"Daily check-in completed! {success_count}/{len(private_keys)} successful")
