## Instructions

### Getting Copilot Pro for free

* [Apply to GitHub Education as a student](https://docs.github.com/en/education/about-github-education/github-education-for-students/apply-to-github-education-as-a-student)

## Requirements and local package install

* Setup directory structure and a few files
    - src/requirements.txt
    - src/user_service/hello.py
    - pyproject.toml
    - tests/test_hello.py: basic unit test, should import user_service.hello

* note: you'll need __init__.py files on the path to packages and tests

* install requirements and local project (from project root)
    - pip install -r src/requirements.txt
    - pip install -e .

## Setup testing

* Setup testing and run test_hello with your IDEs integrated testing.