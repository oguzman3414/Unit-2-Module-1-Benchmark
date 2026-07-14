"""
Automated checks for inventory.py
Run with: python test_inventory.py
(inventory.py must be in the same folder)
"""

import dataclasses

try:
    from inventory import Product, Inventory
except ImportError:
    print("FAIL: Could not import Product/Inventory from inventory.py")
    raise SystemExit(1)


def check(label, condition):
    print(f"{'PASS' if condition else 'FAIL'}: {label}")


def run_tests():
    # 1. Both are actual dataclasses
    check("Product is a dataclass", dataclasses.is_dataclass(Product))
    check("Inventory is a dataclass", dataclasses.is_dataclass(Inventory))

    # 2. Product fields and defaults
    p_fields = {f.name: f for f in dataclasses.fields(Product)}
    check("Product has name, price, quantity, tags fields",
          {"name", "price", "quantity", "tags"} <= p_fields.keys())

    p1 = Product(name="Widget", price=2.5, quantity=10)
    check("Product default quantity/tags work", p1.tags == [] and p1.quantity == 10)

    p2 = Product(name="Gadget", price=1.0)
    p2.tags.append("fragile")
    p3 = Product(name="Gizmo", price=1.0)
    check("Mutable default (tags) is not shared between instances", p3.tags == [])

    # 3. total_value
    p4 = Product(name="Bolt", price=2.0, quantity=5)
    check("total_value() computes price * quantity", p4.total_value() == 10.0)

    # 4. Inventory fields and defaults
    inv = Inventory()
    check("Inventory defaults to empty products list", inv.products == [])

    inv2 = Inventory()
    inv2.products.append(Product(name="X", price=1, quantity=1))
    inv3 = Inventory()
    check("Mutable default (products) is not shared between instances", inv3.products == [])

    # 5. add_product / total_inventory_value / low_stock
    inv = Inventory()
    inv.add_product(Product(name="A", price=10.0, quantity=2))
    inv.add_product(Product(name="B", price=5.0, quantity=20))
    inv.add_product(Product(name="C", price=1.0, quantity=1))

    check("add_product adds to products list", len(inv.products) == 3)
    check("total_inventory_value is correct",
          inv.total_inventory_value() == (10.0 * 2 + 5.0 * 20 + 1.0 * 1))
    check("low_stock returns correct names (default threshold=5)",
          set(inv.low_stock()) == {"A", "C"})
    check("low_stock respects custom threshold",
          set(inv.low_stock(threshold=25)) == {"A", "B", "C"})

    # 6. repr sanity check
    check("Product has an auto-generated repr containing field values",
          "Widget" in repr(p1) and "2.5" in repr(p1))


if __name__ == "__main__":
    run_tests()
