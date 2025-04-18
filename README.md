# Проект ООП (Объектно-Ориентированное Программирование)


Этот проект демонстрирует реализацию принципов объектно-ориентированного программирования (ООП) на языке Python. Включает классы для управления продуктами и категориями, а также юнит-тесты для проверки функциональности.

## Установка

### Предварительные требования

- Убедитесь, что у вас установлен Python (рекомендуется версия 3.8 или выше).
- Установите Poetry, если он еще не установлен. Вы можете установить его, следуя [официальной документации Poetry](https://python-poetry.org/docs/#installation).

### Шаги по установке

1. Клонируйте репозиторий:

   
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   

2. Установите зависимости:
Используйте Poetry для установки всех необходимых зависимостей:

   
    poetry install
    
   
3. Активируйте виртуальную среду:
Poetry автоматически создаст виртуальную среду для вашего проекта. Вы можете активировать её с помощью команды:

    
    poetry shell
    

4. Запустите тесты:
Вы можете запустить тесты с помощью следующей команды:

    
    poetry run pytest --cov=utils tests/ --cov-report=term
   

## Использование

### Пример использования простых классов

from src.utils import Product, Category

# Пример создания категории
electronics_category = Category("Электроника", "Электрические приборы")

# Пример создания продуктов
laptop = Product("Ноутбук", "Мощный ноутбук для работы и игр", 30000.39, 10)
smartphone = Product("Смартфон", "Современный смартфон с камерой 48 МП", 20000.49, 15)

# Пример добавления продуктов в категорию
electronics_category.add_product(laptop)
electronics_category.add_product(smartphone)

print(f"Количество категорий: {Category.category_count}")
print(f"Количество продуктов: {Category.product_count}")

for product in electronics_category.products:
    print(f"Продукт: {product.name}, Цена: {product.price}, Количество: {product.quantity}")

#>>> Количество категорий: 1

    Количество продуктов: 2
    Продукт: Ноутбук, Цена: 30000.39, Количество: 10
    Продукт: Смартфон, Цена: 20000.49, Количество: 15

## Тестирование

В моем проекте используется тестирование для корректности работы. Я использовую фреймвор pytest.
Все написанные мною тесты находятся в папке tests.


```
File         statements  missing  excluded  coverage
src\__init__.py  0         0         0        100%
src\model.py     31        0         0        100%
Total            31        0         0        100%
```