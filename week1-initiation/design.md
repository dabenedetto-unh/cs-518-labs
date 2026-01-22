
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