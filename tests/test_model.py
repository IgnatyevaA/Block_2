import pytest
from src.model import Product, Category

@pytest.fixture()
def sample_product_test():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

@pytest.fixture()
def sample_category_test():
    return Category(
        "Смартфоны",
        "Современные смартфоны с высокими характеристиками",
        [],
    )

def test_check_product(sample_product_test):
    assert sample_product_test.name == "Iphone 15"
    assert sample_product_test.description == "512GB, Gray space"
    assert sample_product_test.price == 210000.0
    assert sample_product_test.price == 8

def test_check_category(sample_category_test):
    assert sample_category_test.name == "Смартфоны"
    assert (
        sample_category_test.description
        == "Современные смартфоны с высокими характеристиками"
    )
    assert sample_category_test.products == []

