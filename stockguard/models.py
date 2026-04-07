"""Models for StockGuard inventory system."""

from dataclasses import dataclass


@dataclass
class Item:
    """Represents an inventory item.

    Args:
        name (str): The name of the item.
        qty (int): The quantity of the item in stock. Must be greater than 0.
        price (float): The price of the item. Must be greater than 0.

    Raises:
        ValueError: If qty is not greater than 0 or price is not greater than 0.
    """
    name: str
    qty: int
    price: float

    def __post_init__(self):
        """Validate qty and price after initialization."""
        if self.qty <= 0:
            raise ValueError("Quantity must be greater than 0")
        if self.price <= 0:
            raise ValueError("Price must be greater than 0")