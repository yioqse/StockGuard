"""Funciones de almacenamiento para el sistema de inventario StockGuard."""

import json
import os


INVENTORY_FILE = 'inventory.json'


def load_inventory() -> list:
    """Cargar el inventario desde un archivo JSON.

    Returns:
        list: Lista de elementos del inventario.
            Devuelve lista vacía si el archivo no existe o el JSON está corrupto.

    Raises:
        FileNotFoundError: Si el archivo no existe (se maneja internamente
            y devuelve []).
        json.JSONDecodeError: Si el JSON es inválido (se maneja internamente
            y devuelve []).
    """
    if not os.path.exists(INVENTORY_FILE):
        return []
    try:
        with open(INVENTORY_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        # Registrar el error o manejar según sea necesario; por ahora devuelve []
        return []


def save_inventory(items: list) -> None:
    """Guardar el inventario en un archivo JSON.

    Args:
        items (list): Lista de elementos de inventario para guardar.

    Nota:
        Guarda con sangría para mejorar la legibilidad.
    """
    with open(INVENTORY_FILE, 'w') as f:
        json.dump(items, f, indent=2)
