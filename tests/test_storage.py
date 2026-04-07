import json

from stockguard.storage import INVENTORY_FILE, load_inventory, save_inventory


def test_load_inventory_nonexistent_file(mocker):
    mocker.patch("stockguard.storage.os.path.exists", return_value=False)

    assert load_inventory() == []


def test_load_inventory_corrupt_file(mocker):
    mocker.patch("stockguard.storage.os.path.exists", return_value=True)
    mocker.patch("stockguard.storage.open", mocker.mock_open(read_data="invalid json"), create=True)
    mocker.patch(
        "stockguard.storage.json.load",
        side_effect=json.JSONDecodeError("Expecting value", "invalid json", 0),
    )

    assert load_inventory() == []


def test_save_inventory_uses_indent_2(mocker):
    fake_open = mocker.mock_open()
    mocker.patch("stockguard.storage.open", fake_open, create=True)
    json_dump = mocker.patch("stockguard.storage.json.dump")

    items = [{"name": "Widget", "qty": 5, "price": 3.99}]
    save_inventory(items)

    json_dump.assert_called_once()
    called_args = json_dump.call_args[0]
    called_kwargs = json_dump.call_args[1]

    assert called_args[0] == items
    assert called_kwargs["indent"] == 2
    assert called_args[1] == fake_open.return_value
