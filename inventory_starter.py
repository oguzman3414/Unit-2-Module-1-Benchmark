"""
Inventory System - Starter Code
Fill in the TODOs to complete the dataclasses benchmark.
"""

from dataclasses import dataclass, field


@dataclass
class Product:
    # TODO: add fields -> name (str), price (float),
    # quantity (int, default 0), tags (list[str], safe default)
    pass

    def total_value(self):
        # TODO: return price * quantity
        pass


@dataclass
class Inventory:
    # TODO: add field -> products (list[Product], safe default)
    pass

    def add_product(self, product):
        # TODO: append product to self.products
        pass

    def total_inventory_value(self):
        # TODO: sum total_value() across all products
        pass

    def low_stock(self, threshold=5):
        # TODO: return list of product names where quantity < threshold
        pass


if __name__ == "__main__":
    # TODO:
    # 1. Create an Inventory
    # 2. Add at least 3 Products (vary quantities, at least one < 5)
    # 3. Print total inventory value, formatted to 2 decimal places
    # 4. Print low-stock product names
    # 5. Print one Product directly to show the auto-generated __repr__
    pass
