# PyMongo

PyMongo is the official Python driver for MongoDB. It allows you to interact with your database using Python dictionaries, making it one of the most natural ways to handle NoSQL data.

Below is an essentials tutorial covering setup, CRUD operations, and best practices for 2026.

---

## 1. Environment Setup

First, install the library using `pip`. It is recommended to use a virtual environment to keep your dependencies clean.

```bash
# Install PyMongo
pip install pymongo

# For SRV connection strings (common with MongoDB Atlas)
pip install "pymongo[srv]"

```

---

## 2. Connecting to the Database

The `MongoClient` object is your gateway to the database. You can connect to a local instance or a cloud cluster like MongoDB Atlas.

```python
from pymongo import MongoClient

# Local Connection
client = MongoClient("mongodb://localhost:27017/")

# Cloud Connection (Atlas)
# uri = "mongodb+srv://<user>:<password>@cluster.mongodb.net/"
# client = MongoClient(uri)

# Access a specific database
db = client["my_app_db"]

# Access a collection (similar to a table in SQL)
users = db["users"]

```

---

## 3. CRUD Operations

CRUD stands for **Create, Read, Update, and Delete**. These are the four basic functions of persistent storage.

### Create (Insert)

You can insert a single document or many at once. MongoDB will automatically add a unique `_id` if you don't provide one.

```python
# Insert one
user_data = {"name": "Alice", "age": 30, "tags": ["python", "dev"]}
result = users.insert_one(user_data)
print(f"Inserted ID: {result.inserted_id}")

# Insert many
user_list = [
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]
users.insert_many(user_list)

```

### Read (Find)

Queries use a dictionary-based syntax. `find_one()` returns a single document, while `find()` returns a cursor you can iterate over.

```python
# Find one by attribute
alice = users.find_one({"name": "Alice"})

# Find many with a filter (e.g., age > 25)
# $gt = Greater Than
for user in users.find({"age": {"$gt": 25}}):
    print(user["name"])

```

### Update

Updates use the `$set` operator to modify specific fields without overwriting the entire document.

```python
# Update one
users.update_one(
    {"name": "Alice"}, 
    {"$set": {"age": 31}}
)

# Update many (add a field to all users)
users.update_many({}, {"$set": {"active": True}})

```

### Delete

Be careful with `delete_many()`, as an empty filter `{}` will wipe the entire collection.

```python
# Delete one
users.delete_one({"name": "Bob"})

# Delete all inactive users
users.delete_many({"active": False})

```

---

## 4. Best Practices for 2026

* **Connection Pooling:** Instantiate `MongoClient` once per process and reuse it. The driver handles connection pooling automatically.
* **Use Context Managers:** For short-lived scripts, use `with MongoClient(...) as client:` to ensure connections are closed properly.
* **Security:** Never hardcode credentials. Use environment variables or a `.env` file to store your connection strings.
* **Type Hinting:** In modern Python, use type hints to make your database logic more readable and easier to debug.
