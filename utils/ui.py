# -*- coding: utf-8 -*-
"""Rich-style UI utilities for Plume Network Testnet Bot — CMD look"""

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import box

console = Console(force_terminal=True, color_system="auto")


# ─── Banner ─────────────────────────────────────────────────────────────────
BANNER_TEXT = r"""
██████╗ ██╗     ██╗   ██╗███╗   ███╗███████╗    ███╗   ██╗███████╗████████╗██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗
██╔══██╗██║     ██║   ██║████╗ ████║██╔════╝    ████╗  ██║██╔════╝╚══██╔══╝██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝
██████╔╝██║     ██║   ██║██╔████╔██║█████╗      ██╔██╗ ██║█████╗     ██║   ██║ █╗ ██║██║   ██║██████╔╝█████╔╝ 
██╔═══╝ ██║     ██║   ██║██║╚██╔╝██║██╔══╝      ██║╚██╗██║██╔══╝     ██║   ██║███╗██║██║   ██║██╔══██╗██╔═██╗ 
██║     ███████╗╚██████╔╝██║ ╚═╝ ██║███████╗    ██║ ╚████║███████╗   ██║   ╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗
╚═╝     ╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝    ╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
                                                                                                                
        ████████╗███████╗███████╗████████╗██╗  ██╗███████╗████████╗    ██████╗  ██████╗ ████████╗              
        ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██║  ██║██╔════╝╚══██╔══╝    ██╔══██╗██╔═══██╗╚══██╔══╝              
           ██║   █████╗  ███████╗   ██║   ███████║█████╗     ██║       ██████╔╝██║   ██║   ██║                 
           ██║   ██╔══╝  ╚════██║   ██║   ██╔══██║██╔══╝     ██║       ██╔══██╗██║   ██║   ██║                 
           ██║   ███████╗███████║   ██║   ██║  ██║███████╗   ██║       ██████╔╝╚██████╔╝   ██║                 
           ╚═╝   ╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝   ╚═╝       ╚═════╝  ╚═════╝    ╚═╝                 
"""


def print_banner():
    """Print main banner in cyan-blue style"""
    subtitle = "[dim cyan]Python 3.8+  │  Automated Faucet Claims  │  Transaction Management[/]"
    panel = Panel(
        Text.from_markup(f"[bold cyan]{BANNER_TEXT}[/]\n\n{subtitle}"),
        box=box.DOUBLE_EDGE,
        border_style="cyan",
        padding=(0, 2),
    )
    console.print(panel)


# ─── Menu Table ─────────────────────────────────────────────────────────────
def show_menu_table(menu_items: list) -> str:
    """Display menu as cyan-blue themed table"""
    table = Table(
        show_header=True,
        header_style="bold cyan",
        border_style="cyan",
        box=box.SQUARE_DOUBLE_HEAD,
        title="[bold cyan] PLUME NETWORK TESTNET BOT MENU [/]",
        title_style="cyan",
        expand=True,
    )
    table.add_column("#", style="cyan bold", justify="center", width=4)
    table.add_column("Action", style="bright_cyan")
    table.add_column("Description", style="grey58")
    
    for key, action, desc in menu_items:
        table.add_row(key, action, desc)
    
    console.print()
    console.print(table)
    return console.input("\n[bold cyan]Select action: [/]").strip()


# ─── Generic Tables ─────────────────────────────────────────────────────────
def show_results_table(title: str, headers: list, rows: list):
    """Display results table"""
    table = Table(
        show_header=True,
        header_style="bold cyan",
        border_style="cyan",
        box=box.SIMPLE_HEAD,
        title=f"[bold cyan] {title} [/]",
        title_style="cyan",
    )
    
    for header in headers:
        if isinstance(header, tuple):
            name, style, justify, width = header
            table.add_column(name, style=style, justify=justify, width=width)
        else:
            table.add_column(header, style="bright_cyan")
    
    for row in rows:
        table.add_row(*[str(cell) for cell in row])
    
    console.print()
    console.print(table)
    console.print()


def show_simple_list(title: str, items: list):
    """Show simple bullet list inside a panel"""
    body = "\n".join(f"[cyan]•[/] {item}" for item in items)
    panel = Panel(
        Text.from_markup(body),
        title=f"[bold cyan] {title} [/]",
        border_style="cyan",
        box=box.ROUNDED,
    )
    console.print()
    console.print(panel)
    console.print()


# ─── Message helpers ────────────────────────────────────────────────────────
def print_success(msg: str):
    console.print(f"[green]✓[/] {msg}")


def print_error(msg: str):
    console.print(f"[red]✗[/] {msg}")


def print_info(msg: str):
    console.print(f"[cyan]i[/] {msg}")


def print_warning(msg: str):
    console.print(f"[yellow]![/] {msg}")


def separator(char: str = "═", length: int = 60):
    console.print("[dim]" + char * length + "[/]")


def input_pause():
    """Wait for user to press Enter"""
    console.input("\n[dim]Press Enter to return to menu...[/]")
