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
            raise TypeError("Можно складывать только объекты одного и того же класса")
        return self.price * self.quantity + other.price * other.quantity


class Smartphone(Product):
    def __init__(
        self, name: str, description: str, price: float, quantity: int,
        performance: str, model: str, storage: str, color: str
    ):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.storage = storage
        self.color = color


class LawnGrass(Product):
    def __init__(
        self, name: str, description: str, price: float, quantity: int,
        country_of_origin: str, growth_time: str, color: str
    ):
        super().__init__(name, description, price, quantity)
        self.country_of_origin = country_of_origin
        self.growth_time = growth_time
        self.color = color


class Category:
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.__products = []  # Приватный атрибут
        Category.total_categories += 1

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты типа Product или его наследники")
        if not any(p.name == product.name for p in self.__products):
            Category.total_unique_products += 1
        self.__products.append(product)

    @property
    def products(self):
        return [
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self.__products
        ]

    def __len__(self):
        return sum(product.quantity for product in self.__products)

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self)} шт."
