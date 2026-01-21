# Mapper and repository

For the first part of this course, we will be developing a user management / authentication package.

The package will use:
* pydantic for validation
* pymongo / mongoDB for database

If you didn't set up the repo directory structure last week, please do so now.

* [setup](../week1-initiation/lab1.1-setup.md)

Everyone on the team should have pulled the latest code.

* cd to project root
* run: ```git pull```

## Instructions

### Gettting Copilot Pro for free

* [Apply to GitHub Education as a student](https://docs.github.com/en/education/about-github-education/github-education-for-students/apply-to-github-education-as-a-student)

### Preparing the prompt

Getting started:

* Work individually at first.  
* In "docs/prompts/", create these files: 
    - "initial-prompt.md"
    - "prompt-log.md"

Provide context information:

* about your app and the Epic.  
* about the architecture and tech stack.

Ask for these assets to be generated in your src/user_service directory:

* models.py: pydantic models for users
* mapper.py: maps between pydantic models and python dicts
* repository.py: takes users, converts to dict, and inserts into database
* exceptions.py: custom exceptions raised by the repository

and these tests in your tests/test_user_service:

* test_mapper.py: unit tests for mapper
* test_repository.py: unit tests for repository

### Generating the code

* Open the chat panel:
    - View > Chat, OR
    - Ctrl + Alt + I
* With your prompt file open, you should see a button in the lower-right with a plus sign that allows you to "Enable current file context".
    - Ask Agent to carry out the instructions in the prompt file.

### Testing

If you haven't done so already, you need to setup testing in your IDE.

* [setup testing](../week1-initiation/notes/1.1.3_setup_testing.md)

If you have any errors loading tests, you'll need to resolve them.

If not:
* Run test_user_mapper.py using the IDE integration.
* If that works, run test_user_repository.py

If any tests fail, you'll have to resolve the issues through a combination of 
* manual intervention / coding
* using a web/chat AI interface 
* using copilot

## Reporting

<!-- Source code and tests should be added to your Gitlab repository (in "src/user_service" and "tests/user_service" respectively) -->

Submission:
* Documentation should be added to a lab report document, which is added to your "docs" directory.
* You will also submit your lab report on Canvas.

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
