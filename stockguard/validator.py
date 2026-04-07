"""Validation functions for StockGuard inventory system."""


def validate_qty(qty: int) -> bool:
    """Validate that quantity is greater than 0.

    Args:
        qty (int): The quantity to validate.

    Returns:
        bool: True if qty > 0, False otherwise.

    Raises:
        ValueError: If qty is not an integer or is <= 0.

    Example:
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
    """Validate that price is greater than 0.

    Args:
        price (float): The price to validate.

    Returns:
        bool: True if price > 0, False otherwise.

    Raises:
        ValueError: If price is not a number or is <= 0.

    Example:
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