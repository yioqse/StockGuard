import pytest

from stockguard.validator import validate_price, validate_qty


test_values_qty_valid = [1, 10, 1000000000]

test_values_qty_invalid = [0, -1, -1000]

test_values_price_valid = [0.01, 1, 1000000.0, 999999999]

test_values_price_invalid = [0, -0.01, -100]


@pytest.mark.parametrize("qty", test_values_qty_valid)
def test_validate_qty_valid(qty):
    assert validate_qty(qty) is True


@pytest.mark.parametrize("qty", test_values_qty_invalid)
def test_validate_qty_invalid(qty):
    with pytest.raises(ValueError, match="Quantity must be greater than 0"):
        validate_qty(qty)


def test_validate_qty_invalid_type():
    with pytest.raises(ValueError, match="integer"):
        validate_qty(3.5)


@pytest.mark.parametrize("price", test_values_price_valid)
def test_validate_price_valid(price):
    assert validate_price(price) is True


@pytest.mark.parametrize("price", test_values_price_invalid)
def test_validate_price_invalid(price):
    with pytest.raises(ValueError, match="Price must be greater than 0"):
        validate_price(price)


def test_validate_price_invalid_type():
    with pytest.raises(ValueError, match="number"):
        validate_price("free")
