class Category:
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.__products = []  # Приватный атрибут
        Category.total_categories += 1

    def add_product(self, product):
        if not any(p.name == product.name for p in self.__products):
            Category.total_unique_products += 1
        self.__products.append(product)

    @property
    def products(self):
        return [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
                for product in self.__products]


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price  # Приватный атрибут
        self.quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Цена не может быть отрицательной")
        self._price = value

    @price.deleter
    def price(self):
        del self._price

    @classmethod
    def create_product(cls, **kwargs):
        return cls(**kwargs)
