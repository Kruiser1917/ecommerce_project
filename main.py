from src.shop import Category, Product

# Пример создания объектов классов
electronics = Category("Electronics", "Gadgets and devices")
laptop = Product.create_product("Laptop", "A personal computer for mobile use", 999.99, 10)
smartphone = Product.create_product("Smartphone", "A portable device that combines mobile telephone and computing "
                                                  "functions", 499.99, 5)

# Добавление продуктов в категорию
electronics.add_product(laptop)
electronics.add_product(smartphone)

# Проверка созданных объектов и общего количества категорий и уникальных продуктов
print(f"Category: {electronics.name}, Description: {electronics.description}")
for product in electronics.products:
    print(product)

print(f"Total Categories: {Category.total_categories}")
print(f"Total Unique Products: {Category.total_unique_products}")
