# Pydantic Basics

Pydantic is the most widely used data validation library for Python. It uses Python type hints to enforce data schemas, sanitize input, and provide clear error messages.

## 1. Defining a Model

To create a Pydantic model, define a class that inherits from `BaseModel`. Each attribute requires a type hint.

```python
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: int
    username: str
    email: str
    bio: Optional[str] = None  # Optional field with a default value

```

## 2. Creating Objects

You can instantiate Pydantic models in two primary ways.

### Direct Instantiation

Passing data as keyword arguments.

```python
user_1 = User(id=1, username="dev_jake", email="jake@example.com")
print(user_1.username) # Output: dev_jake

```

### From a Dictionary

Commonly used when receiving JSON data from an API.

```python
external_data = {
    "id": 2,
    "username": "sarah_codes",
    "email": "sarah@example.com"
}

user_2 = User.model_validate(external_data)

```

## 3. Sanitization & Coercion

Pydantic is a **parsing** library, not just a validation library. It attempts to "coerce" data into the correct type if possible.

```python
# 'id' is passed as a string, but will be converted to an integer
user_3 = User(id="100", username="coerced_user", email="test@test.com")

print(type(user_3.id)) 
# Output: <class 'int'>

```

## 4. Dumping Data (Serialization)

Exporting your validated objects back to standard Python dictionaries or JSON strings is simple.

```python
# Convert to Dictionary
print(user_1.model_dump())

# Convert to JSON String
print(user_1.model_dump_json())

```

## 5. Basic Validation

If data cannot be coerced (e.g., providing letters for an integer field), Pydantic raises a `ValidationError`.

```python
from pydantic import ValidationError

try:
    # 'id' expects an int, but gets a non-numeric string
    invalid_user = User(id="abc", username="oops", email="oops@test.com")
except ValidationError as e:
    print(e.json())

```

## 6. Validation with `Field`

Use `Field` to add constraints that go beyond simple types, such as string lengths or numeric ranges.

```python
from pydantic import Field

class Product(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    price: float = Field(..., gt=0)  # Must be Greater Than 0
    stock: int = Field(default=0, ge=0) # Must be Greater/Equal to 0

# This would fail validation if price was -1.0

```

## 7. Nested Models

Models can be nested within one another to represent complex data structures.

```python
class Address(BaseModel):
    city: str
    state: str

class Employee(BaseModel):
    name: str
    address: Address  # Nested reference

data = {
    "name": "Alice",
    "address": {"city": "New York", "state": "NY"}
}

emp = Employee.model_validate(data)
print(emp.address.city) # Output: New York

```

---

### Summary Table

| Feature | Method / Syntax |
| --- | --- |
| **New Object** | `Model(field=value)` |
| **From Dict** | `Model.model_validate(my_dict)` |
| **To Dict** | `model_obj.model_dump()` |
| **To JSON** | `model_obj.model_dump_json()` |
| **Constraints** | `Field(gt=0, min_length=2)` |
