# Lab 3: Repository

Usual reporting and workflow requirements apply:

* [workflow](../general/workflow.md)
* [reporting](../general/reporting.md)

## About the repository

The Repository interfaces with the database.

* Its methods take and return pydantic model objects (e.g. User)
* It uses the Mapper to convert between pydantic objects and dict-like objects.
* It handles exception cases and raises custom exceptions, for example:
    - on creation: duplicate username or email
    - on retrieval: user not found 

In order to generate the repository, copilot needs to know about:

* your pydantic models (src/user_service/models.py)
* the Mapper (src/user_service/mapper.py)
* what DB driver you are using (pymongo; see notes)
* what testing framework (unittest; see notes)

With copilot, you should generate:

* src/user_service/repository.py - defined the Repository class
* src/user_service/exceptions.py - defines custom exceptions
* tests/test_user_service/test_repository.py - unit tests for Repository

## Notes

Notes:

- DB / driver:
    - the default for this course is pymongo.
    - you are also free to user "motor," which is like pymongo but asynchronous.
- test framework:
    - default is unittest
    - you are also free to use pytest.
- **disclaimer:** 
    - demos will be given using the defaults