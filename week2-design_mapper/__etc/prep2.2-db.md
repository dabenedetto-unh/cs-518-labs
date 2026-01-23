# Database 1 prep

## Setting up MongoDB

### Setup

To work with MongoDB

* Install mongoDB locally
    * https://www.mongodb.com/docs/manual/administration/install-community/
* DO install mongoDB compass

### Connecting to MongoDB Atlas

* Setup a MongoDB Atlas account and create a free cluster

Login to mongoDB Atlas in your browser:

* Database > Clusters > Create / Connect > Drivers
    - Copy URI (starts with mongodb+srv)
* Security > DB Access > Users
    - Get username and password
    - update <password> in your URI

(Save the URI for later, you will use it on pymongo_prep below)

### Configuring Atlas for access from anywhere

* Sign into MongoDB Atlas
* Security > Network Access > Add IP Address
* Add this Entry: 0.0.0.0/0

## Working with pymongo

### Tutorials

Review pymongo tutorial(s):
- https://pymongo.readthedocs.io/en/stable/tutorial.html 
- https://www.w3schools.com/python/python_mongodb_getstarted.asp 

### Key concepts

Review pymongo tutorial(s) for key concepts:
* Connect to Db
    - Use the URI from above to connect to your DB
* CRUD operations: 
    - Create: Adding new records to a database (insert)
    - Read: Retrieving data from a database (find)
    - Update: Modifying existing records in a database (update)
    - Delete: Removing existing records from a database (delete)

<!-- ## Prep reading / response

The goal is to ensure that you are prepared for the lab.  Responses should be 150 to 300 words (about 2–3 short paragraphs).

Components:
* The "Pivot" (50–75 words): Identify one specific concept from the reading and explain how it differs from how they previously thought about coding.
* The "Technical Connection" (50–75 words): How does this concept apply to the upcoming lab's specific codebase or tool?
* The "Blocker" (25–50 words): One specific question or "muddiest point" they want addressed before the lab starts.

Most prep assignments involve code.  In these cases, you should include some code snippets in your response, but code snippets do not count towards your overall word count.

When you submit a response with code, you should use markdown with code blocks (see below), or jupyter notebook (ipynb).

```python
print("Hello, World!")
``` -->

## FAQ

### ServerSelectionTimeoutError Fix

If you happen to receive an error with the message "ServerSelectionTimeoutError [SSL: CERTIFICATE_VERIFY_FAILED]..." while trying to connect to MongoDB, this seems to be caused by MongoDB's digital certificate not appearing on your computer's trusted certificate list for some reason.

To fix this, you can install the "certifi" module on your machine (either through pip or your IDE's Python module manager), and then modify your __init__ function in DBManager.py by changing:

* "myclient = pymongo.MongoClient(conn_str)" to
* "myclient = pymongo.MongoClient(conn_str, tlsCAFile=certifi.where())"
