# Mapper

In this lab, you will:

* implement models, source code, and tests for a Mapper.
* document and report your work (lab2_2-reporting.md)

## Workflow for individual and group work

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

## Working with Copilot

Getting started:

* Make sure that your IDE is open at the root of your project
* Make sure you're on your own branch for lab 2. 

### The prompt

* In "docs/prompts/", create these files: 
    - "lab2-prompt.md"

Your prompt should include context and instructions.
For at least this first time, I will provide a prompt.
We will all use the same one and see how our results compare.

* [prompt](files/lab2-prompt.md)

Notes / thoughts:

* Is it a good idea for this to be just one prompt?
* It might make more sense to generate models first, and iterate on that, then use that as an input for generating the Mapper.

### Generating the code

* Open the chat panel:
    - View > Chat, OR
    - Ctrl + Alt + I
* With your prompt file open, you should see a button in the lower-right with a plus sign that allows you to "Enable current file context".
    - Ask Agent to carry out the instructions in the prompt file.

## Testing

If you have any errors loading tests, you'll need to resolve them.

If not:
* Run test_user_mapper.py using the IDE integration.

If any tests fail, you'll have to resolve the issues through a combination of 
* manual intervention / coding
* using a web/chat AI interface 
* using copilot

## Submission and rubric

## Adding your work to Gitlab

* One team member pushes the code and tests to the group repo,
    - src/user_service/
    - tests/user_service/
* After all of your work is pushed to the remote repo, everyone on your team should sync their local repos:
    - ```git pull```

### Submission

* Consolidate your prompts and discussion in a lab report:
* Push the lab report to your group repo, here:
    - docs/reports/lab1-report.md
* More information about reporting:
    * [reporting](../general/reporting.md)
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