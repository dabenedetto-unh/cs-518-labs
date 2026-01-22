## Lab 1: Planning and design

Instructions:

* see here for more info about reporting:
    - [reporting](notes/reporting.md)

* Your work will go here:
    * Save your process docs in "docs/reports/" directory.
    * Save final planning and design file(s) in markdown (.md) in the "docs/designs" folder in your repo.

* You will also submit to Canvas:
    * URL for your repo

After all of your work is pushed to the remote repo, everyone on your team should sync their local repos:

```git pull```

## Part 1: Planning

Get into pairs or groups of 3.

* Come up with an app idea.
* Ask AI to develop vision, epics, and user stories.  Save your prompt.
* Discuss with your peers.

## Part 2: Architectural Design

2.a. Architecture

* What is software architecture?
* Ask AI to compare monolithic, service-oriented, and microservice architectures.
* Discuss and document.

2.b. Your idea

* Ask AI to generate design diagrams for your App.  In your prompt, please include:
    - context: information about your app 
    - request: ask for an ERD and a simple (monolithic) architecture diagram
    - ask it to use mermaid.ai and provide the response in JSON format
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

<!-- ## Stack

2.b. Tech stack

* What is a tech stack?
* Ask AI to discuss pros / cons of various tech stacks.
* Discuss with your peers. -->

