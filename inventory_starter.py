"""
Inventory System - Starter Code
Fill in the TODOs to complete the dataclasses benchmark.
"""

from dataclasses import dataclass, field


@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0
    tags: list[str] = field(default_factory=list)

    def total_value(self):
        return self.price * self.quantity


@dataclass
class Inventory:
    products: list[Product] = field(default_factory=list)

    def add_product(self, product):
        self.products.append(product)

    def total_inventory_value(self):
        return sum(product.total_value() for product in self.products)

    def low_stock(self, threshold=5):
        return [product.name for product in self.products if product.quantity < threshold]


if __name__ == "__main__":
    # 1. Create an Inventory
    inventory = Inventory()

    # 2. Add at least 3 Products
    inventory.add_product(Product("Laptop", 999.99, 10, ["electronics"]))
    inventory.add_product(Product("Mouse", 24.99, 3, ["electronics", "accessory"]))
    inventory.add_product(Product("Keyboard", 49.99, 7, ["electronics"]))
    inventory.add_product(Product("Charger", 50.99, 2, ["electronics", "accessory"]))

    # 3. Print total inventory value, formatted to 2 decimal places
    print(f"Total inventory value: ${inventory.total_inventory_value():.2f}")

    # 4. Print low-stock product names
    print("Low-stock products:", inventory.low_stock())

    # 5. Print one Product directly to show the auto-generated __repr__
    print(inventory.products[0])