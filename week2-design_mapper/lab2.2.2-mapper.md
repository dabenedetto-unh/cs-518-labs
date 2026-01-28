# Models and Mapper

We will create User models and a Mapper.
The Mapper is used to convert between these models.

In this lab, you will:

* implement / generate Pydantic models, a Mapper class, and tests for the Mapper.
* document and report your work.

There is a specific workflow to follow for labs from now on.  For more information, see:

* [workflow](../general/workflow.md)

## Working with Copilot

Getting started:

* Make sure that your IDE is open at the root of your project
* Make sure you're on your own branch for lab 2. 

### The prompt

* In "docs/prompts/", create a file using a clear naming convention, e.g.: 
    - "02_2-models_mapper.md"
* Your prompt(s) should include at least:
    - User fields
    - relevant architecture details
    - tools and testing framework
    - output files, format, locations
* You can find example prompts in the demo project, here:
    - [demo project](https://gitlab.cs.unh.edu/cs518-public/spring-2026/class-demo)

### Generating the code

* Open the chat panel:
    - View > Chat, OR
    - Ctrl + Alt + I
* Select a model
    - I got much better results when I used "Gemini 3 Flash," than using the default "Auto."  You are welcome to experiment with different models.    
* With your prompt file open, you should see a button in the lower-right with a plus sign that allows you to "Enable current file context".
    - Ask Agent to carry out the instructions in the prompt file.

## Testing

* If you have any errors loading tests, you'll need to resolve them.
* If not:
    * Run test_user_mapper.py using the IDE integration.
* If any tests fail, you'll have to resolve the issues through a combination of 
    * manual intervention / coding
    * using a web/chat AI interface 
    * using copilot
    * or other means

## Submission and rubric

* More information about workflow and reporting:
    * [workflow](../general/workflow.md)
    * [reporting](../general/reporting.md)

### Adding your work to Gitlab

* One team member pushes the code and tests to the group repo
* After all of your work is pushed to the remote repo, everyone on your team should sync their local repos:
    - ```git pull```

### Submission

* Consolidate your prompts and discussion in a lab report:
* Push the lab report to your group repo, here:
    - docs/reports/lab1-report.md
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