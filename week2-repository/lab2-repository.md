# Mapper and repository

For the first part of this course, we will be using this architecture and stack:

* Architecture:
    * monolithic architecture
    * controller-service-repository pattern for backend
* Tech stack:
    * full-stack python
    * flask for app (with basic jinja templates)
    * pydantic for validation
    * pymongo / mongoDB for database

And developing this epic:

* User management / authentication

## Instructions

### Preparing the prompt

Work in different pairs or small groups.

Create two files:

* context.txt
* prompt.txt

In the context file, you should provide information:

* about your app and the Epic.  
* about the architecture and tech stack.

In the prompt, you should ask for these files in JSON format:

* models: pydantic models for users
* mapper: maps between pydantic models and python dicts
* repository: takes users, converts to dict, and inserts into database
* exceptions: custom exceptions raised by the repository

and these tests:

* test_mapper: unit tests for mapper
* test_repository: unit tests for repository

### Generating the response

Some options:

* (A) use the basic chat interface.  I've been using Gemini, but you are free to use others.
* (B) use an API.  Gemini API has a free tier, but you need to provide a credit card.
* (C) use integrated IDE tools, e.g. VSCode Copilot or Roo.

Disclaimer: IDE tools are powerful but can mangle your codebase.

### Parsing the response

you will need to parse the response to create the files. 
You can do this with a script.

* prompt: "please provide a script that will parse a json file with filenames and contents and create the files"

### Testing

Finally, you will need to setup testing in your IDE.

* https://code.visualstudio.com/docs/debugtest/testing

## Reporting

Source code and tests should be added to your Gitlab repository (in "src/user_service" and "tests/user_service" respectively)
All other documentation should be added to a lab report document, which is added to your "docs" directory.

**Lab report: a single document containing:**
 
* **Verification:** A screenshot of your VSCode "Testing" panel showing all tests passed.
* **Prompt evolution log**
* **Group discussion synthesis**
* **Other questions.**

In addition to adding to your repo, please submit the report to Canvas.

### 1. The "Final" Source Code & Test Report

* **Source code:** Submitted to your Gitlab repository in the "src/user_service" directory
* **Tests:** Submitted to Gitlab repo in the "tests/test_user_service" directory 
* **A screenshot of the Test Explorer:** A visual confirmation that all tests passed (the "Green Checkmarks").  

### 2. The "Prompt Evolution" Log

* **The initial prompt:** What they started with.
* **The iterations:** If the first code failed the tests, what did they change in the prompt to fix it?
* **Reflection:** A 2-3 sentence summary of *why* the AI failed initially (e.g., "The AI didn't handle the empty list case correctly, so I had to explicitly mention edge cases").

### 3. The Group Discussion Synthesis

"Code Commentary." Table or list.  For each function:

* Function name
* What the Test specifically checked
* One thing the group learned/noticed

### 4. Other questions

* Please discuss the function of each of the core components (mapper, repository).
* Please discuss the role of the models and exceptions.
    - what is exception translation?  how does that apply here.
* please review the unit tests.
    - it is very likely that your tests use unittest.mock.  What is mocking?  why would you use mocking in unit testing?
