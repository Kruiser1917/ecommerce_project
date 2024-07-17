from src.shop import Category, Product, Smartphone, LawnGrass

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
    "name": "iPhone",
    "description": "Apple smartphone",
    "price": 799.99,
    "quantity": 5,
    "performance": "High",
    "model": "13 Pro",
    "storage": "256GB",
    "color": "Black"
}
lawn_grass_data = {
    "name": "Premium Grass",
    "description": "High quality lawn grass",
    "price": 19.99,
    "quantity": 50,
    "country_of_origin": "USA",
    "growth_time": "10 days",
    "color": "Green"
}

laptop = Product.create_product(**laptop_data)
smartphone = Smartphone(**smartphone_data)
lawn_grass = LawnGrass(**lawn_grass_data)

# Добавление продуктов в категорию
electronics.add_product(laptop)
electronics.add_product(smartphone)
electronics.add_product(lawn_grass)

# Проверка созданных объектов и общего количества категорий и уникальных продуктов
print(f"Category: {electronics.name}, Description: {electronics.description}")
for product in electronics.products:
    print(product)

print(f"Total Categories: {Category.total_categories}")
print(f"Total Unique Products: {Category.total_unique_products}")

# Пример использования магических методов
print(f"Category details: {electronics}")
print(f"Product details: {laptop}")

try:
    total_value = laptop + smartphone
except TypeError as e:
    print(e)

total_value = laptop + Product("Another Laptop", "Another laptop description", 799.99, 5)
print(f"Total value of products: {total_value} руб.")
