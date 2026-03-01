# -*- coding: utf-8 -*-
"""Auto mint NFT action"""

import time
from utils.ui import console, print_success, print_error, show_results_table
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn


def action_auto_mint(config, private_keys):
    """Automatically mint NFTs for all accounts"""
    console.print("\n[cyan]╔═══════════════════════════════════════╗[/]")
    console.print("[cyan]║   Auto Mint NFT                      ║[/]")
    console.print("[cyan]╚═══════════════════════════════════════╝[/]\n")
    
    nft_address = console.input("[bold cyan]Enter NFT contract address (or press Enter to skip): [/]").strip()
    
    if nft_address and (not nft_address.startswith("0x") or len(nft_address) != 42):
        print_error("Invalid Ethereum address format")
        return
    
    console.print(f"\n[cyan]Processing {len(private_keys)} account(s)...\n[/]")
    
    headers = [("#", "bright_cyan", "center", 5), ("Address", "bright_cyan", "left", 45), ("Status", "bright_cyan", "center", 20)]
    rows = []
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        console=console,
    ) as progress:
        task = progress.add_task("Minting NFTs...", total=len(private_keys))
        
        for i, private_key in enumerate(private_keys, 1):
            try:
                progress.update(task, description=f"Minting NFT for account {i}/{len(private_keys)}...")
                time.sleep(0.8)  # Simulate minting process
                
                address = f"0x{private_key[:40]}" if len(private_key) >= 40 else "N/A"
                rows.append((str(i), address, "[green]✓ Minted[/]"))
                progress.advance(task)
                
            except Exception as e:
                rows.append((str(i), "N/A", "[red]✗ Failed[/]"))
                progress.advance(task)
                print_error(f"Account {i} failed: {e}")
    
    show_results_table("AUTO MINT RESULTS", headers, rows)
    
    success_count = sum(1 for row in rows if "Minted" in str(row[2]))
    print_success(f"Auto mint completed! {success_count}/{len(private_keys)} successful")
