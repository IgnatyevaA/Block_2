class Product:
    def __init__(self, name, description, price, quality):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quality

class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count = sum(product.quantity for product in self.products)
