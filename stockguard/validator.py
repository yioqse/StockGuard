"""Funciones de validación para el sistema de inventario StockGuard."""


def validate_qty(qty: int) -> bool:
    """Validar que la cantidad sea un entero positivo.

    Args:
        qty (int): Cantidad a validar.

    Returns:
        bool: True si qty > 0, False en caso contrario.

    Raises:
        ValueError: Si qty no es un entero o es <= 0.

    Ejemplo:
        >>> validate_qty(5)
        True
        >>> validate_qty(0)
        Traceback (most recent call last):
            ValueError: Quantity must be greater than 0
    """
    if not isinstance(qty, int):
        raise ValueError("Quantity must be an integer")
    if qty <= 0:
        raise ValueError("Quantity must be greater than 0")
    return True


def validate_price(price: float) -> bool:
    """Validar que el precio sea un valor positivo.

    Args:
        price (float): Precio a validar.

    Returns:
        bool: True si price > 0, False en caso contrario.

    Raises:
        ValueError: Si price no es un número o es <= 0.

    Ejemplo:
        >>> validate_price(10.5)
        True
        >>> validate_price(-5.0)
        Traceback (most recent call last):
            ValueError: Price must be greater than 0
    """
    if not isinstance(price, (int, float)):
        raise ValueError("Price must be a number")
    if price <= 0:
        raise ValueError("Price must be greater than 0")
    return True
