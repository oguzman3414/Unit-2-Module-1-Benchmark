# Coding Benchmark: Python Dataclasses

**Goal:** Build a small inventory system using `dataclasses` to show you understand fields, default values, methods, and `__post_init__`.

---

## Task

Create a file called `inventory.py` that implements the following.

### 1. `Product` dataclass

Create a dataclass called `Product` with these fields:

| Field | Type | Notes |
|---|---|---|
| `name` | `str` | required |
| `price` | `float` | required |
| `quantity` | `int` | default `0` |
| `tags` | `list[str]` | default: empty list (use a safe default!) |

Add a method `total_value(self)` that returns `price * quantity`.

### 2. `Inventory` dataclass

Create a second dataclass called `Inventory` with:

| Field | Type | Notes |
|---|---|---|
| `products` | `list[Product]` | default: empty list (use a safe default!) |

Add these methods:

- `add_product(self, product)` — appends a `Product` to `products`.
- `total_inventory_value(self)` — returns the sum of `total_value()` across all products.
- `low_stock(self, threshold=5)` — returns a list of product names where `quantity < threshold`.

### 3. Demo script

At the bottom of `inventory.py`, under `if __name__ == "__main__":`, write code that:

1. Creates an `Inventory`.
2. Adds at least 3 `Product` instances (varying quantities, at least one below 5).
3. Prints the total inventory value, formatted to 2 decimal places.
4. Prints the list of low-stock product names.
5. Prints one `Product` directly (e.g. `print(product)`) to show the auto-generated `__repr__`.

---

## Requirements Checklist (how you'll be graded)

- [ ] Both classes use `@dataclass`
- [ ] No hand-written `__init__` methods (let the decorator generate them)
- [ ] Mutable defaults (`tags`, `products`) use a safe pattern — **not** `field: list = []`
- [ ] `total_value()` and `total_inventory_value()` return correct numeric results
- [ ] `low_stock()` returns the correct product names
- [ ] Demo script runs without errors and prints all 5 required outputs
- [ ] Code runs top to bottom with: `python inventory.py`

---

## Starter Code

A starter file (`inventory_starter.py`) is provided with the class shells and TODOs — fill it in.

## Automated Check

A test file (`test_inventory.py`) is provided. Once you've written `inventory.py`, run:

```
python test_inventory.py
```

All tests should print `PASS`.
