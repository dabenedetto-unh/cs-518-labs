# Designs

In this lab, you will:

* create a design document (lab2_1-designs.md) that contains your architectural designs for your app idea.
* document and report your work (lab2_1-reporting.md)

## Concepts / discussion

* What is software architecture?
* Ask AI to compare monolithic, service-oriented, and microservice architectures.
* Discuss and document.

## Ideation

* ERD:
    * Brainstorm about entities and relationships for your app (with or without AI)
    * Ask AI to generate an ERD. (see below for tips)
* Architecture:
    * Brainstorm about services for your app
    * Ask AI to generate an architecture diagram - with monolithic architecture.
    * Ask AI to generate a diagram with microservices diagram.
* Iteration and discussion
    * Discuss and iterate, as needed.
    
## Using mermaid.ai

Here's a tip for generating diagrams with AI:

* you can ask AI to generate "code" for a diagram using mermaid.ai
* Generate links for your diagrams.
    - option A: using mermaid.live.  (expand "actions" in lower-left to get image URL)
    - option B: using a script with the code below

```python
# graph = THE_GENERATED_GRAPH_TEXT
graphbytes = graph.encode("ascii")
base64_bytes = base64.b64encode(graphbytes)
base64_string = base64_bytes.decode("ascii")

diagrams_out[name] = f"https://mermaid.ink/img/{base64_string}"
```

## Submission and rubric

## Adding your work to Gitlab

* Push the final design document to your group repo, here:
    - docs/planning/lab2-designs.md
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

* report
    - prompt log
    - discussion summary
* design document
    - contains descriptions of entities and relationships
    - diagram: ERD
    - contains overview of services
    - diagram: architecture diagrams
        - monolithic
        - MSA