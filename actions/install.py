# -*- coding: utf-8 -*-
"""Install dependencies action"""

import subprocess
import sys
from utils.ui import console, print_success, print_error


def action_install_dependencies():
    """Install Python dependencies"""
    console.print("\n[cyan]📦 Installing dependencies...\n[/]")
    
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
            check=True,
            capture_output=True,
            text=True
        )
        print_success("Dependencies installed successfully!")
        if result.stdout:
            console.print(result.stdout)
    except subprocess.CalledProcessError as e:
        print_error("Failed to install dependencies")
        if e.stderr:
            console.print(f"[red]{e.stderr}[/]")
    except FileNotFoundError:
        print_error("pip not found. Make sure Python is installed correctly.")
    except Exception as e:
        print_error(f"Unexpected error: {e}")
