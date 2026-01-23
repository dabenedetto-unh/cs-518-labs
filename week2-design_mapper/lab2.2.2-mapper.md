# Mapper

Individual work:

* Individuals will work on their own branch
    * This way, everyone can generate their own code.
* As you go, you can push your branch to the remote regularly.
* Carefully read and review code that you're generating.

Group work:

* Discuss your code with your group.
* Choose one version to keep.
* That student merges their branch into main and pushes main to remote

For more information, see:

* [workflow](../general/workflow.md)
* [reporting](../general/reporting.md)

Individual reporting via. exit tickets.

### Preparing the prompt

Getting started:

* Make sure that your IDE is open at the root of your project
* Make sure you're on your own branch for lab 2. 
* In "docs/prompts/", create these files: 
    - "lab2-prompt.md"
    - "prompt-log.md"

### The prompt

Your prompt should include context and instructions.
For at least this first time, I will provide a prompt.
We will all use the same one and see how our results compare.

```md
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
    * models.py: pydantic models for User.
    * mapper.py: maps between pydantic models and python dicts.
* tests/
    * test_mapper.py: unit tests for Mapper.
```

### Generating the code

* Open the chat panel:
    - View > Chat, OR
    - Ctrl + Alt + I
* With your prompt file open, you should see a button in the lower-right with a plus sign that allows you to "Enable current file context".
    - Ask Agent to carry out the instructions in the prompt file.

### Testing

If you have any errors loading tests, you'll need to resolve them.

If not:
* Run test_user_mapper.py using the IDE integration.

If any tests fail, you'll have to resolve the issues through a combination of 
* manual intervention / coding
* using a web/chat AI interface 
* using copilot
