# Context

* langage: python
* validation: pydantic
* testing framework: unittest

# Instructions

* Create models and a mapper for User.
* A User has:
    - id: str
    - username
    - password
    - email 
    - role: "admin" or "user" 

# Output

* src/
    * user_service/
        * models.py: pydantic models for User.
        * mapper.py: maps between pydantic models and python dicts.
* tests/
    * user_service/
        * test_mapper.py: unit tests for Mapper.