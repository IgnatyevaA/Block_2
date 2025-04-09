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
    assert sample_product_test.title == "Iphone 15"
    assert sample_product_test.details == "512GB, Gray space"
    assert sample_product_test.cost == 210000.0
    assert sample_product_test.amount == 8

def test_check_category(sample_category_test):
    assert sample_category_test.label == "Смартфоны"
    assert (
        sample_category_test.info
        == "Современные смартфоны с высокими характеристиками"
    )
    assert sample_category_test.items == []

