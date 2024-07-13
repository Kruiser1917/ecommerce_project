import pytest
from src.shop import Category, Product
import sys
import os

# Добавление корневой директории проекта в путь поиска модулей
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture
def category():
    return Category("Electronics", "Gadgets and devices")


@pytest.fixture
def product():
    return Product("Laptop", "A personal computer for mobile use", 999.99, 10)


def test_category_initialization(category):
    assert category.name == "Electronics"
    assert category.description == "Gadgets and devices"
    assert isinstance(category._products, list)
    assert len(category._products) == 0


def test_product_initialization(product):
    assert product.name == "Laptop"
    assert product.description == "A personal computer for mobile use"
    assert product.price == 999.99
    assert product.quantity == 10


def test_add_product_to_category(category, product):
    initial_unique_products = Category.total_unique_products
    category.add_product(product)
    assert len(category._products) == 1
    assert category._products[0] == product
    assert Category.total_unique_products == initial_unique_products + 1


def test_category_products_output(category, product):
    category.add_product(product)
    assert category.products == ["Laptop, 999.99 руб. Остаток: 10 шт."]


def test_create_product():
    product = Product.create_product("Smartphone", "A portable device", 499.99, 5)
    assert product.name == "Smartphone"
    assert product.description == "A portable device"
    assert product.price == 499.99
    assert product.quantity == 5


def test_product_price_getter(product):
    assert product.price == 999.99


def test_product_price_setter(product):
    product.price = 1099.99
    assert product.price == 1099.99
    with pytest.raises(ValueError):
        product.price = -100


def test_product_price_deleter(product):
    del product.price
    with pytest.raises(AttributeError):
        _ = product.price


if __name__ == "__main__":
    pytest.main()
