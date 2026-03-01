# -*- coding: utf-8 -*-
"""Configuration loader for Plume Network Testnet Bot"""

import os
import json
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Default configuration
DEFAULT_CONFIG = {
    "RPC_URL": "https://phoenix-rpc.plumenetwork.xyz",
    "FAUCET_URL": "https://faucet.plumenetwork.xyz",
    "CHAIN_ID": 161221135,
}


def load_config():
    """Load configuration from .env file"""
    config = DEFAULT_CONFIG.copy()
    
    # Override with environment variables if they exist
    config["RPC_URL"] = os.getenv("RPC_URL", config["RPC_URL"])
    config["FAUCET_URL"] = os.getenv("FAUCET_URL", config["FAUCET_URL"])
    config["CHAIN_ID"] = int(os.getenv("CHAIN_ID", config["CHAIN_ID"]))
    
    return config


def load_private_keys():
    """Load private keys from privateKeys.json"""
    private_keys_path = Path(__file__).parent / "privateKeys.json"
    
    if not private_keys_path.exists():
        return []
    
    try:
        with open(private_keys_path, "r", encoding="utf-8") as f:
            keys = json.load(f)
            if isinstance(keys, list):
                return [key.strip() for key in keys if key.strip()]
            return []
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error loading private keys: {e}")
        return []


def save_private_keys(keys: list):
    """Save private keys to privateKeys.json"""
    private_keys_path = Path(__file__).parent / "privateKeys.json"
    
    try:
        with open(private_keys_path, "w", encoding="utf-8") as f:
            json.dump(keys, f, indent=2, ensure_ascii=False)
        return True
    except IOError as e:
        print(f"Error saving private keys: {e}")
        return False
