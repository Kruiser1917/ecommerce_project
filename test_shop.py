import pytest
from main import Category, Product  # Импортируйте ваши классы из основного файла


@pytest.fixture
def category():
    return Category("Electronics", "Gadgets and devices")


@pytest.fixture
def product():
    return Product("Laptop", "A personal computer for mobile use", 999.99, 10)


def test_category_initialization(category):
    assert category.name == "Electronics"
    assert category.description == "Gadgets and devices"
    assert isinstance(category.products, list)
    assert len(category.products) == 0


def test_product_initialization(product):
    assert product.name == "Laptop"
    assert product.description == "A personal computer for mobile use"
    assert product.price == 999.99
    assert product.quantity == 10


def test_add_product_to_category(category, product):
    initial_unique_products = Category.total_unique_products
    category.add_product(product)
    assert len(category.products) == 1
    assert category.products[0] == product
    assert Category.total_unique_products == initial_unique_products + 1


def test_total_categories():
    initial_total_categories = Category.total_categories
    Category("Books", "Various kinds of books")
    assert Category.total_categories == initial_total_categories + 1


def test_total_unique_products(category, product):
    initial_unique_products = Category.total_unique_products
    category.add_product(product)
    new_product = Product("Smartphone", "A portable device", 499.99, 5)
    category.add_product(new_product)
    assert Category.total_unique_products == initial_unique_products + 2


if __name__ == "__main__":
    pytest.main()
