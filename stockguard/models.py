"""Modelos para el sistema de inventario StockGuard."""

from dataclasses import dataclass


@dataclass
class Item:
    """Representa un ítem de inventario.

    Args:
        name (str): Nombre del ítem.
        qty (int): Cantidad del ítem en stock. Debe ser mayor que 0.
        price (float): Precio del ítem. Debe ser mayor que 0.

    Raises:
        ValueError: Si qty no es mayor que 0 o price no es mayor que 0.
    """
    name: str
    qty: int
    price: float

    def __post_init__(self):
        """Validar los campos de cantidad y precio después de la inicialización.

        Raises:
            ValueError: Si qty es menor o igual a 0.
            ValueError: Si price es menor o igual a 0.
        """
        if self.qty <= 0:
            raise ValueError("Quantity must be greater than 0")
        if self.price <= 0:
            raise ValueError("Price must be greater than 0")
