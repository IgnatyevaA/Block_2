from src.model import Product, Category

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1)
    print(product2)
    print(product3)

    category1 = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни")
    category1.add_product(product1)
    category1.add_product(product2)
    category1.add_product(product3)

    print(category1)
    print(category1.products)
    print(Category.category_count)
    print(Category.product_count)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры", "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником")
    category2.add_product(product4)

    print(category2)
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)

    # Пример использования итерации по категории
    for product in category1:
        print(product)
