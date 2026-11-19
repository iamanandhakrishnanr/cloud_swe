import pytest
from buggy import get_last_item

def test_get_last_item_hidden():
    items = ["a", "b", "c"]
    assert get_last_item(items) == "c"

def test_get_last_item_single_element():
    items = [42]
    assert get_last_item(items) == 42