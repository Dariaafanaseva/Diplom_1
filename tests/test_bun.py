import pytest
from practicum.bun import Bun
from data import BUN_NAME, BUN_PRICE, BUN_PRICE_ZERO, BUN_PRICE_NEGATIVE

class TestBun:
    def test_bun_initialization(self):
        bun = Bun(BUN_NAME, BUN_PRICE)
        assert bun.get_name() == BUN_NAME
        assert bun.get_price() == BUN_PRICE

    def test_bun_name(self):
        bun = Bun(BUN_NAME, BUN_PRICE)
        assert bun.get_name() == BUN_NAME

    def test_bun_price(self):
        bun = Bun(BUN_NAME, BUN_PRICE)
        assert bun.get_price() == BUN_PRICE

    def test_bun_negative_price(self):
        bun = Bun(BUN_NAME, BUN_PRICE_NEGATIVE)
        assert bun.get_price() == BUN_PRICE_NEGATIVE

    def test_bun_zero_price(self):
        bun = Bun(BUN_NAME, BUN_PRICE_ZERO)
        assert bun.get_price() == 0.0

    def test_bun_price_type(self):
        bun = Bun(BUN_NAME, BUN_PRICE)
        assert isinstance(bun.get_price(), float)

    def test_bun_name_type(self):
        bun = Bun(BUN_NAME, BUN_PRICE)
        assert isinstance(bun.get_name(), str)

    def test_bun_set_name(self):
        bun = Bun(BUN_NAME, BUN_PRICE)
        bun.name = "Glutten_free"
        assert bun.get_name() == "Glutten_free"

    def test_bun_set_price(self):
        bun = Bun(BUN_NAME, BUN_PRICE)
        bun.price = 109.9
        assert bun.get_price() == 109.9
