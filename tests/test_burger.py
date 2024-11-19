from practicum.burger import Burger
from data import BUN_NAME, BUN_PRICE, INGREDIENT_NAME, INGREDIENT_PRICE, INGREDIENT2_PRICE, INGREDIENT2_NAME
from practicum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestBurger:
    def test_create_burger(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun.get_name() == BUN_NAME
        assert burger.bun.get_price() == BUN_PRICE

    def test_add_ingredient(self, mock_ingredient1):
        burger = Burger()
        burger.add_ingredient(mock_ingredient1)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0].name == INGREDIENT_NAME
        assert burger.ingredients[0].price == INGREDIENT_PRICE
        assert burger.ingredients[0].type == INGREDIENT_TYPE_SAUCE

    def test_remove_ingredient(self, mock_ingredient1):
        burger = Burger()
        burger.add_ingredient(mock_ingredient1)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, mock_ingredient1, mock_ingredient2):
        burger = Burger()
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.move_ingredient(0,1)
        assert burger.ingredients[0].name == INGREDIENT2_NAME
        assert burger.ingredients[0].price == INGREDIENT2_PRICE
        assert burger.ingredients[0].type == INGREDIENT_TYPE_FILLING

    def test_get_price_burger(self, mock_bun, mock_ingredient1):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        assert burger.get_price() == 398.8

    def test_get_price_burger_type(self, mock_bun, mock_ingredient1):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        assert isinstance(burger.get_price(), float)

    def test_get_receipt(self, mock_bun, mock_ingredient1, mock_ingredient2):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        total_price = mock_bun.get_price()*2 + mock_ingredient1.get_price() + mock_ingredient2.get_price()
        expected_receipt = (
            f'(==== {mock_bun.get_name()} ====)\n'  
            f'= {mock_ingredient1.get_type().lower()} {mock_ingredient1.get_name()} =\n'  
            f'= {mock_ingredient2.get_type().lower()} {mock_ingredient2.get_name()} =\n'  
            f'(==== {mock_bun.get_name()} ====)\n'
            f'\nPrice: {total_price:.1f}')
        assert burger.get_receipt() == expected_receipt

