# -*- coding: utf-8 -*-
"""About action"""

from rich.panel import Panel
from rich.text import Text
from rich import box
from utils.ui import console, input_pause


def action_about():
    """Show about information"""
    about_text = """
[bold white]Plume Network Testnet Bot[/]

[cyan]Version:[/] 1.0.0
[cyan]License:[/] MIT

[yellow bold]Features:[/]
  • Claim ETH and GOON tokens from Plume testnet faucet
  • Automatically handles transactions and errors
  • Provides real-time feedback and transaction details
  • Daily check-in functionality
  • Auto mint NFT
  • Auto stake
  • Auto swap

[yellow bold]Requirements:[/]
  • Python 3.8+
  • pip for package management
  • .env file for storing sensitive information
  • privateKeys.json for daily check-ins

[yellow bold]Repository:[/]
  https://github.com/frankrichardhall/PlumeNetwork-Testnet-bot.git

[yellow bold]Installation:[/]
  1. Clone the repository
  2. Install dependencies: pip install -r requirements.txt
  3. Copy .env.example to .env and configure
  4. Copy privateKeys.json.example to privateKeys.json and add your keys
  5. Run: python main.py
    """
    
    panel = Panel(
        Text.from_markup(about_text),
        title="[bold cyan] ABOUT [/]",
        border_style="cyan",
        box=box.ROUNDED,
        padding=(1, 2),
    )
    
    console.print()
    console.print(panel)
    console.print()
    input_pause()
