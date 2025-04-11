class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        """Геттер для приватного атрибута price."""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер для приватного атрибута price с проверкой на положительное значение."""
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__products = []
        Category.category_count += 1

    def add_product(self, product):
        """Добавляет продукт в список и увеличивает счетчик продуктов."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер для приватного атрибута products."""
        return "\n".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self.__products
        )

    @classmethod
    def new_product(cls, product_data):
        """Создает новый продукт на основе словаря."""
        return Product(
            name=product_data['name'],
            description=product_data['description'],
            price=product_data['price'],
            quantity=product_data['quantity']
        )
