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

    def __len__(self):
        return sum(product.quantity for product in self.__products)

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self)} шт."


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

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __len__(self):
        return self.quantity

    def __add__(self, other):
        if not isinstance(other, Product):
            raise ValueError("Можно складывать только объекты типа Product")
        return self.price * self.quantity + other.price * other.quantity
