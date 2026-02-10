# Lab 3: Repository

* In this lab, you will:
    * implement Repository class, custom exceptions, and tests
    * document and report your work
* For more information, see:
    * [reporting](../general/reporting.md)
    * [workflow](../general/workflow.md)

## About the repository

See the sample prompt in the demo-project

<!-- The Repository interfaces with the database.

* Its methods take and return pydantic model objects (e.g. User)
* It uses the Mapper to convert between pydantic objects and dict-like objects.
* It handles exception cases and raises custom exceptions, for example:
    - on creation: duplicate username or email
    - on retrieval: user not found 

In order to generate the repository, copilot needs to know about:

* your pydantic models (src/user_service/models.py)
* the Mapper (src/user_service/mapper.py)
* what DB driver you are using (pymongo)
* what testing framework (unittest)

With copilot, you should generate:

* src/user_service/repository.py - defined the Repository class
* src/user_service/exceptions.py - defines custom exceptions
* tests/test_user_service/test_repository.py - unit tests for Repository -->

## Submission and rubric

## Adding your work to Gitlab

* One team member pushes the code and tests to the group repo,
* After all of your work is pushed to the remote repo, everyone on your team should sync their local repos:
    - ```git pull```

### Submission

* Consolidate your prompts and discussion in a lab report:
* Push the lab report to your group repo
* Submission (Canvas):
    - For this lab, you should submit your report.

### Rubric

- gitlab:
    - individual branches: pts off for individual if they don't have this
    - group solution: models, tests and mapper
- report
    - prompt log
    - verification / testing
    - discussion summary