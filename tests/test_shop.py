import pytest
from src.shop import Category, Product, Smartphone, LawnGrass
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


@pytest.fixture
def smartphone():
    return Smartphone(
        "iPhone", "Apple smartphone", 799.99, 5, "High", "13 Pro", "256GB", "Black"
    )


@pytest.fixture
def lawn_grass():
    return LawnGrass(
        "Premium Grass", "High quality lawn grass", 19.99, 50, "USA", "10 days", "Green"
    )


def test_category_initialization(category):
    assert category.name == "Electronics"
    assert category.description == "Gadgets and devices"
    assert isinstance(category._Category__products, list)
    assert len(category._Category__products) == 0


def test_product_initialization(product):
    assert product.name == "Laptop"
    assert product.description == "A personal computer for mobile use"
    assert product.price == 999.99
    assert product.quantity == 10


def test_smartphone_initialization(smartphone):
    assert smartphone.name == "iPhone"
    assert smartphone.description == "Apple smartphone"
    assert smartphone.price == 799.99
    assert smartphone.quantity == 5
    assert smartphone.performance == "High"
    assert smartphone.model == "13 Pro"
    assert smartphone.storage == "256GB"
    assert smartphone.color == "Black"


def test_lawn_grass_initialization(lawn_grass):
    assert lawn_grass.name == "Premium Grass"
    assert lawn_grass.description == "High quality lawn grass"
    assert lawn_grass.price == 19.99
    assert lawn_grass.quantity == 50
    assert lawn_grass.country_of_origin == "USA"
    assert lawn_grass.growth_time == "10 days"
    assert lawn_grass.color == "Green"


def test_add_product_to_category(category, product):
    initial_unique_products = Category.total_unique_products
    category.add_product(product)
    assert len(category._Category__products) == 1
    assert category._Category__products[0] == product
    assert Category.total_unique_products == initial_unique_products + 1


def test_add_smartphone_to_category(category, smartphone):
    initial_unique_products = Category.total_unique_products
    category.add_product(smartphone)
    assert len(category._Category__products) == 1
    assert category._Category__products[0] == smartphone
    assert Category.total_unique_products == initial_unique_products + 1


def test_add_lawn_grass_to_category(category, lawn_grass):
    initial_unique_products = Category.total_unique_products
    category.add_product(lawn_grass)
    assert len(category._Category__products) == 1
    assert category._Category__products[0] == lawn_grass
    assert Category.total_unique_products == initial_unique_products + 1


def test_category_products_output(category, product):
    category.add_product(product)
    assert category.products == ["Laptop, 999.99 руб. Остаток: 10 шт."]


def test_create_product():
    product_data = {
        "name": "Smartphone",
        "description": "A portable device",
        "price": 499.99,
        "quantity": 5
    }
    product = Product.create_product(**product_data)
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


def test_product_str(product):
    assert str(product) == "Laptop, 999.99 руб. Остаток: 10 шт."


def test_category_str(category, product):
    category.add_product(product)
    assert str(category) == "Electronics, количество продуктов: 10 шт."


def test_product_len(product):
    assert len(product) == 10


def test_category_len(category, product):
    category.add_product(product)
    assert len(category) == 10


def test_product_add(product):
    other_product = Product("Laptop", "Another laptop", 799.99, 5)
    assert product + other_product == 999.99 * 10 + 799.99 * 5


def test_product_add_type_error(product, smartphone):
    with pytest.raises(TypeError):
        product + smartphone


if __name__ == "__main__":
    pytest.main()
