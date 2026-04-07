# stockguard.py — código heredado (NO modificar este archivo directamente)

import json
import os

INVENTORY_FILE = 'inventory.json'


def load_inventory():
    """Cargar el inventario desde un archivo JSON.

    Returns:
        list: Lista de elementos del inventario.
            Devuelve una lista vacía si el archivo no existe.
    """
    if not os.path.exists(INVENTORY_FILE):
        return []
    with open(INVENTORY_FILE) as f:
        return json.load(f)   # ⚠ sin manejo de JSON corrupto


def save_inventory(items):
    """Guardar el inventario en un archivo JSON.

    Args:
        items (list): Lista de elementos de inventario para guardar.
    """
    with open(INVENTORY_FILE, 'w') as f:
        json.dump(items, f)


def add_item(name, qty, price):
    """Agregar un ítem nuevo al inventario.

    Args:
        name (str): Nombre del ítem.
        qty (int): Cantidad del ítem en stock.
        price (float): Precio del ítem.
    """
    items = load_inventory()
    items.append({'name': name, 'qty': qty, 'price': price})
    save_inventory(items)  # ⚠ acepta qty y price negativos


def update_price(name, new_price):
    """Actualizar el precio de un ítem existente.

    Args:
        name (str): Nombre del ítem a actualizar.
        new_price (float): Nuevo precio del ítem.
    """
    items = load_inventory()
    for item in items:
        if item['name'] == name:
            item['price'] = new_price  # ⚠ sin validar new_price
    save_inventory(items)


def get_total_value():
    """Calcular el valor total del inventario.

    Returns:
        float: Suma de cantidad * precio para todos los ítems del inventario.
    """
    return sum(i['qty'] * i['price'] for i in load_inventory())
