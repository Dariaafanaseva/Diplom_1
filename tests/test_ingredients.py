import pytest
from practicum.ingredient import Ingredient
from practicum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import INGREDIENT_NAME, INGREDIENT_PRICE

class TestIngredient:
    def test_create_ingredient_filling(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, INGREDIENT_NAME, INGREDIENT_PRICE)
        assert ingredient.type == INGREDIENT_TYPE_FILLING
        assert ingredient.name == INGREDIENT_NAME
        assert ingredient.price == INGREDIENT_PRICE

    def test_create_ingredient_sauce(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, INGREDIENT_NAME, INGREDIENT_PRICE)
        assert ingredient.type == INGREDIENT_TYPE_SAUCE
        assert ingredient.name == INGREDIENT_NAME
        assert ingredient.price == INGREDIENT_PRICE

    def test_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, INGREDIENT_NAME, INGREDIENT_PRICE)
        assert ingredient.get_price() == INGREDIENT_PRICE

    def test_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, INGREDIENT_NAME, INGREDIENT_PRICE)
        assert ingredient.get_name() == INGREDIENT_NAME

    def test_get_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, INGREDIENT_NAME, INGREDIENT_PRICE)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
