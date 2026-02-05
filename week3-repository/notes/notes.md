# Day 1: 

* Intro to Pydantic
* Discussion of Mapper
--
* Review development workflow
* Generating code

# Day 2:

## Review generated models

    - A
        - UserRole
        - UserBase
    - B
        - UserCreate
        - UserUpdate
        - User - domain model
        - UserDocument - represents a record in DB
            - why isn't this inheriting from UserBase?
    - missing?
        - UserOut (*)

(*) this is a result of the prompt:  "Mapper maps between user input (dicts), Pydantic User model objects, and pymongo database documents."  The prompt never said anything about mapping to output / response objects.
    - whether or not this is problem is TBD

## Discuss models

    - User
        - ```from_attributes```
            - allows the model to communicate with non-dictionary objects—specifically those that use dot notation
            - not needed
    - UserDocument
        - ```id: str = Field(..., alias="_id")```
            - MongoDB stores the primary key as _id, but Python variables starting with underscore are conventionally private.
            - The alias allows automatic mapping: when reading from the database, _id becomes id; when writing back, id becomes _id
        - ```populate_by_name```
            - allows the UserDocument model to accept data using either the field name or its alias.

## Review Mapper

Mapper tests:

    "user_service.test_mapper": {
        "TestUserMapper": [
            "test_create_to_user",          # UserCreate to User    Service uses this when it hashes the pw
            "test_dict_to_user_create",     # input to UserCreate   Controller will use to validate and parse input
            "test_document_to_user",        # document to User      Repository will use this for DB retrieval
            "test_user_to_document"         # User to document,     Repository will use this for DB insertion
        ]
    },

Recall:

* I/O -> controller -> service -> repository -> database

Notes:

* for now, probably don't need a UserOut model, since the password will be hashed and the other fields are safe for output.

## Wrapping up the Mapper

* individual students make sure that they push their own branch
* discuss and decide which solution to merge and push to main
* pull main