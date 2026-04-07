# stockguard.py — código heredado (NO modificar este archivo directamente)

import json
import os

INVENTORY_FILE = 'inventory.json'


def load_inventory():
    """Cargar el inventario desde el archivo JSON.

    Returns:
        list: Lista de elementos en el inventario. Si el archivo no existe o
            el contenido no es JSON válido, devuelve una lista vacía.

    Ejemplo:
        >>> load_inventory()
        []
    """
    if not os.path.exists(INVENTORY_FILE):
        return []
    with open(INVENTORY_FILE) as f:
        return json.load(f)   # ⚠ sin manejo de JSON corrupto


def save_inventory(items):
    """Guardar el inventario en un archivo JSON.

    Args:
        items (list): Lista de elementos a guardar en el inventario.

    Ejemplo:
        >>> save_inventory([{"name": "Widget", "qty": 1, "price": 9.99}])
        None
    """
    with open(INVENTORY_FILE, 'w') as f:
        json.dump(items, f)


def add_item(name, qty, price):
    """Agregar un ítem nuevo al inventario.

    Args:
        name (str): Nombre del ítem.
        qty (int): Cantidad del ítem.
        price (float): Precio del ítem.

    Ejemplo:
        >>> add_item('Widget', 5, 2.5)
        None
    """
    items = load_inventory()
    items.append({'name': name, 'qty': qty, 'price': price})
    save_inventory(items)  # ⚠ acepta qty y price negativos


def update_price(name, new_price):
    """Actualizar el precio de un ítem existente.

    Args:
        name (str): Nombre del ítem a actualizar.
        new_price (float): Nuevo precio del ítem.

    Ejemplo:
        >>> update_price('Widget', 3.99)
        None
    """
    items = load_inventory()
    for item in items:
        if item['name'] == name:
            item['price'] = new_price  # ⚠ sin validar new_price
    save_inventory(items)


def get_total_value():
    """Calcular el valor total de inventario.

    Returns:
        float: Suma de qty * price para todos los ítems del inventario.

    Ejemplo:
        >>> get_total_value()
        0
    """
    return sum(i['qty'] * i['price'] for i in load_inventory())
