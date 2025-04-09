class Product:
    def __init__(self, title, details, cost, amount):
        self.title = title
        self.details = details
        self.cost = cost
        self.amount = amount

class Category:
    total_items = 0
    total_groups = 0

    def __init__(self, label, info, items):
        self.label = label
        self.info = info
        self.items = items
        Category.total_groups += 1
        Category.total_items += len(items)
