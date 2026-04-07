"""Storage functions for StockGuard inventory system."""

import json
import os


INVENTORY_FILE = 'inventory.json'


def load_inventory() -> list:
    """Load inventory from JSON file.

    Returns:
        list: List of inventory items. Returns empty list if file not found or corrupted.

    Raises:
        FileNotFoundError: If the file does not exist (handled internally, returns []).
        json.JSONDecodeError: If the JSON is invalid (handled internally, returns []).
    """
    if not os.path.exists(INVENTORY_FILE):
        return []
    try:
        with open(INVENTORY_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        # Log error or handle as needed, for now return empty list
        return []


def save_inventory(items: list) -> None:
    """Save inventory to JSON file.

    Args:
        items (list): List of inventory items to save.

    Note:
        Saves with indentation for readability.
    """
    with open(INVENTORY_FILE, 'w') as f:
        json.dump(items, f, indent=2)