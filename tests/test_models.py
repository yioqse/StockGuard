import pytest

from stockguard.models import Item


def test_item_creation_valid():
    item = Item(name="Widget", qty=10, price=1.99)

    assert item.name == "Widget"
    assert item.qty == 10
    assert item.price == 1.99


@pytest.mark.parametrize("qty", [0, -5])
def test_item_invalid_qty(qty):
    with pytest.raises(ValueError, match="Quantity must be greater than 0"):
        Item(name="Widget", qty=qty, price=1.99)


@pytest.mark.parametrize("price", [0, -1.0])
def test_item_invalid_price(price):
    with pytest.raises(ValueError, match="Price must be greater than 0"):
        Item(name="Widget", qty=5, price=price)


def test_item_edge_case_large_qty_and_small_price():
    item = Item(name="MegaPack", qty=10**9, price=0.001)

    assert item.qty == 10**9
    assert item.price == 0.001
