class Category:
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.products = []
        Category.total_categories += 1

    def add_product(self, product):
        if not any(p.name == product.name for p in self.products):
            Category.total_unique_products += 1
        self.products.append(product)


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


# Пример создания объектов классов
electronics = Category("Electronics", "Gadgets and devices")
laptop = Product("Laptop", "A personal computer for mobile use", 999.99, 10)
smartphone = Product(
    "Smartphone",
    "A portable device that combines mobile telephone and computing functions",
    499.99,
    5
)

# Добавление продуктов в категорию
electronics.add_product(laptop)
electronics.add_product(smartphone)

# Проверка созданных объектов и общего количества категорий и уникальных продуктов
print(f"Category: {electronics.name}, Description: {electronics.description}")
for product in electronics.products:
    print(
        f"Product: {product.name}, Description: {product.description}, "
        f"Price: {product.price}, Quantity: {product.quantity}"
    )


print(f"Total Categories: {Category.total_categories}")
print(f"Total Unique Products: {Category.total_unique_products}")
