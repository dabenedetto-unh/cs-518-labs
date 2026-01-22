# Prep: Pydantic & MongoDB

This assignment prepares you for the upcoming lab by setting up your data validation tools (**Pydantic**) and your database environment (**MongoDB**).

## Step 1: Software Installation

You must install the database software locally and the Python libraries via the terminal.

### 1. Local Database Tools

* **MongoDB Community Server:** Download and install the version for your OS: [MongoDB Community Download](https://www.mongodb.com/try/download/community).
* **MongoDB Compass:** This is a visual "GUI" for your database. **Ensure you install this** during the MongoDB setup process.

### 2. Python Libraries

Open your terminal or command prompt and run:

```bash
# Data validation (may already be installed from last week)
pip install pydantic

# Database driver for Python
pip install pymongo

# Helper to fix potential SSL/Connection errors
pip install certifi
```

---

## Step 2: Cloud Database Setup (MongoDB Atlas)

1. **Create an Account:** Sign up for a free tier at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).
2. **Network Access:** In Atlas, go to **Security > Network Access** and add IP address `0.0.0.0/0`. This ensures you can connect from the school or home Wi-Fi.
3. **Connection URI:** Go to **Database > Connect > Drivers** and copy your URI (starts with `mongodb+srv://`). Replace `<password>` with your database user password and save this string for the lab.

---

## Step 3: Required Reading

* **Pydantic:** Read [Basic Model Usage](https://docs.pydantic.dev/latest/concepts/models/) and **Data Conversion**. Pay attention to how Pydantic "coerces" types (e.g., turning a string `"5"` into an integer `5`).
* **PyMongo:** Review the [PyMongo Tutorial](https://pymongo.readthedocs.io/en/stable/tutorial.html) for **CRUD** operations: **C**reate, **R**ead, **U**pdate, and **D**elete.

---

## Step 4: Submission Requirements

Your response should be **150 to 300 words** (roughly 2–3 short paragraphs) and submitted to Canvas.

### Components:

1. **The Pivot (50–75 words):** Identify one specific concept from the reading (like Pydantic's automatic validation or NoSQL document storage) and explain how it differs from how you previously thought about coding.
2. **The Technical Connection (50–75 words):** How does this concept apply to the upcoming lab? Specifically, how will Pydantic models help us manage the data we save into MongoDB?
3. **The Blocker (25–50 words):** What is one specific question or "muddiest point" you want addressed before the lab starts?