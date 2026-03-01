# -*- coding: utf-8 -*-
"""Claim GOON tokens from faucet"""

import requests
from utils.ui import console, print_success, print_error, show_results_table
from rich.progress import Progress, SpinnerColumn, TextColumn


def action_claim_goon(config):
    """Claim GOON tokens from faucet"""
    console.print("\n[cyan]╔═══════════════════════════════════════╗[/]")
    console.print("[cyan]║   Claim GOON Tokens from Faucet      ║[/]")
    console.print("[cyan]╚═══════════════════════════════════════╝[/]\n")
    
    address = console.input("[bold cyan]Enter your wallet address: [/]").strip()
    
    if not address:
        print_error("Address cannot be empty")
        return
    
    # Validate address format (basic check)
    if not address.startswith("0x") or len(address) != 42:
        print_error("Invalid Ethereum address format")
        return
    
    faucet_url = config.get("FAUCET_URL", "https://faucet.plumenetwork.xyz")
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("Claiming GOON tokens from faucet...", total=None)
        
        try:
            response = requests.post(
                f"{faucet_url}/goon",
                json={"address": address},
                timeout=30
            )
            
            if response.status_code == 200:
                progress.update(task, completed=True)
                print_success("GOON tokens claimed successfully!")
                
                data = response.json()
                headers = [("Field", "bright_cyan", "left", 20), ("Value", "grey58", "left", 50)]
                rows = [
                    ("Address", address),
                    ("Status", data.get("status", "Success")),
                ]
                
                if "txHash" in data:
                    rows.append(("Transaction Hash", data["txHash"]))
                if "amount" in data:
                    rows.append(("Amount", f"{data['amount']} GOON"))
                
                show_results_table("TRANSACTION DETAILS", headers, rows)
            else:
                progress.update(task, completed=True)
                print_error(f"Failed to claim GOON tokens. Status: {response.status_code}")
                if response.text:
                    console.print(f"[red]Response: {response.text}[/]")
                    
        except requests.exceptions.RequestException as e:
            progress.update(task, completed=True)
            print_error(f"Network error: {e}")
        except Exception as e:
            progress.update(task, completed=True)
            print_error(f"Unexpected error: {e}")
