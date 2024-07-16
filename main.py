from src.shop import Category, Product

# Пример создания объектов классов
electronics = Category("Electronics", "Gadgets and devices")

# Используем метод create_product с распаковкой аргументов
laptop_data = {
    "name": "Laptop",
    "description": "A personal computer for mobile use",
    "price": 999.99,
    "quantity": 10
}
smartphone_data = {
    "name": "Smartphone",
    "description": "A portable device that combines mobile telephone and computing functions",
    "price": 499.99,
    "quantity": 5
}

laptop = Product.create_product(**laptop_data)
smartphone = Product.create_product(**smartphone_data)

# Добавление продуктов в категорию
electronics.add_product(laptop)
electronics.add_product(smartphone)

# Проверка созданных объектов и общего количества категорий и уникальных продуктов
print(f"Category: {electronics.name}, Description: {electronics.description}")
for product in electronics.products:
    print(product)

print(f"Total Categories: {Category.total_categories}")
print(f"Total Unique Products: {Category.total_unique_products}")

# Пример использования магических методов
print(f"Category details: {electronics}")
print(f"Product details: {laptop}")

total_value = laptop + smartphone
print(f"Total value of products: {total_value} руб.")
