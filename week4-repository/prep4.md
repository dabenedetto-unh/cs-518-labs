(note for spring 2026 - This was already completed as part of the prep2)

# Prep: Pymongo and MongoDB

## Step 1: Software Installation

You must install the database software locally and the Python libraries via the terminal.

### 1. Local Database Tools

* **MongoDB Community Server:** Download and install the version for your OS: [MongoDB Community Download](https://www.mongodb.com/try/download/community).
* **MongoDB Compass:** This is a visual "GUI" for your database. **Ensure you install this** during the MongoDB setup process.

### 2. Python Libraries

Open your terminal or command prompt and run:

```bash
# Database driver for Python
pip install pymongo
```

---

## Step 2: Cloud Database Setup (MongoDB Atlas)

Creating account and cluster:
- **Create an Account:** Sign up for a free tier at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).
- **Create a Cluster**  Choose the Free option and create a Deployment.

Configuring user and network access
- **Create a Db User**
- **Configure Network Access:** Ensure that `0.0.0.0/0` is on the access list.
- Note:
    - You can also configure these under **Security > Database & Network Access** 

Getting your connection URI:
- **Connection URI:** Go to **Database > Clusters** and click "Connect"
    - Then, select "Drivers" and copy the connection string (starts with `mongodb+srv://`). 
    - Replace `<db_username>:<db_password>` with your database username and password and save this string for the lab.

---

## Required Reading

* **PyMongo:** Review the [PyMongo Tutorial](https://pymongo.readthedocs.io/en/stable/tutorial.html)   
    - Read up to "CRUD operations"

* When you do the reading, run the examples and take notes.

---

## Submission Requirements

Same requirements as last time.