import pytest
from src.model import Product, Category

@pytest.fixture()
def sample_product_test():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

@pytest.fixture()
def sample_category_test():
    return Category("Смартфоны", "Современные смартфоны с высокими характеристиками")

def test_check_product(sample_product_test):
    assert sample_product_test.name == "Iphone 15"
    assert sample_product_test.description == "512GB, Gray space"
    assert sample_product_test.price == 210000.0
    assert sample_product_test.quantity == 8

def test_check_category(sample_category_test):
    assert sample_category_test.name == "Смартфоны"
    assert sample_category_test.description == "Современные смартфоны с высокими характеристиками"
    assert sample_category_test.products == ""

def test_add_product(sample_category_test, sample_product_test):
    sample_category_test.add_product(sample_product_test)
    assert "Iphone 15, 210000.0 руб. Остаток: 8 шт." in sample_category_test.products
    assert Category.product_count == 1

def test_price_setter(sample_product_test):
    sample_product_test.price = 220000.0
    assert sample_product_test.price == 220000.0

    sample_product_test.price = -100
    assert sample_product_test.price == 220000.0

def test_new_product():
    product_data = {
        'name': 'Laptop',
        'description': '16GB RAM, 512GB SSD',
        'price': 60000.0,
        'quantity': 10
    }
    new_product = Category.new_product(product_data)
    assert new_product.name == 'Laptop'
    assert new_product.price == 60000.0

def test_product_str(sample_product_test):
    assert str(sample_product_test) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."

def test_category_str(sample_category_test, sample_product_test):
    sample_category_test.add_product(sample_product_test)
    assert str(sample_category_test) == "Смартфоны, количество продуктов: 8 шт."

def test_product_addition(sample_product_test):
    product2 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    result = sample_product_test + product2
    assert result == 210000.0 * 8 + 180000.0 * 5
