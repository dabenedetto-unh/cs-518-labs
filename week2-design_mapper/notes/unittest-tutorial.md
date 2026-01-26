## 1. The Basic Structure

To create a test, you need to:

1. **Import** the `unittest` module.
2. **Create a class** that inherits from `unittest.TestCase`.
3. **Write methods** that start with the word `test_`. (This prefix is required so the runner knows which methods are tests).

### Example Code

Let's say we want to test a simple addition function.

```python
import unittest

# The function we want to test
def add(a, b):
    return a + b

class TestMathOperations(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()

```

---

## 2. Common Assertions

Assertions are the heart of your tests. They check if the actual output matches your expected output.

| Method | Checks that... |
| --- | --- |
| `assertEqual(a, b)` |  |
| `assertNotEqual(a, b)` |  |
| `assertTrue(x)` | `bool(x)` is True |
| `assertFalse(x)` | `bool(x)` is False |
| `assertIn(item, list)` | `item` is in `list` |
| `assertRaises(Error)` | A specific exception is raised |

---

## 3. Setup and Teardown

Sometimes you need to prepare a database connection or create a temporary file before every test. `unittest` provides two special methods for this:

* **`setUp()`**: Runs **before** every individual test method.
* **`tearDown()`**: Runs **after** every individual test method.

```python
class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = ["User1", "User2"] # Pre-test setup

    def test_user_exists(self):
        self.assertIn("User1", self.db)

    def tearDown(self):
        self.db.clear() # Clean up after test

```

---

## 4. How to Run Your Tests

You can run your tests directly from your terminal. If your file is named `test_logic.py`, use:

```bash
python -m unittest test_logic.py

```

For more detailed output (showing exactly which tests passed or failed), add the **verbose** flag:

```bash
python -m unittest -v test_logic.py

```

---

## Summary Checklist

* [ ] Method names **must** start with `test_`.
* [ ] Use `self.assertEqual()` rather than the standard `assert` keyword for better error messages.
* [ ] Use `setUp()` to keep your code DRY (Don't Repeat Yourself).