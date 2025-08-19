# Module 5: Approaches to Improving AI Agent Reasoning

## Progress

- [x] 01. Improving AI Agent Reasoning with In-Context Learning
  - what is it: show LLMs **correct examples** how to solve a task. Watching the professor [demonstrates how LLM learns patterns through ing in context learning](https://d3c33hcgiwev3.cloudfront.net/EZGyfmroR3O7q_kw4sD1zA.mediaconvert/full/EZGyfmroR3O7q_kw4sD1zA_54467f59a832434e8afd3c43c9a8f6f1_InContextLearning_MP4_720.mp4?Expires=1755734400&Signature=cTloqdYL0-og9ft188xwI1RZLqsmRAx-IaJz41bMPfCZSEz5AarqJ2kWBvB73Vl6f1~t4jZWqIBbFvS7mO1n00aXDU-NxMUBnhQ2oLAtL6Q~X-~rOP4NyxvNkW7WBmaEytAZmQlqjaXxBWUbqlDrBjpG2n7ClZE7-bx09s~1YRw_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) gives you a more direct impression.
  - rationale:
    - LLMs are trained to predict the next word
    - The examples listed in the prompt show LLM a pattern it wants to follow / learn
  - performance: it is incredibly powerful for agents
- [x] 02. Improving AI Agent Reasoning with Up-front Planning & Chain of Thought.
    > but often it can be really effective if we have it think about plans up front.
  - to improve understanding, first visit [this diagram](http://raw.githubusercontent.com/reboottime/ML-in-LLM-Era/refs/heads/main/courses/Introduction%20to%20Generative%20AI%202024/notes/screenshots/angent.png) to understand how Agent works, then visit [this example](./02.upfront-planning-example.md) to compare the difference between reasoning with ad hoc approach and with upfront planing approach.
  - magic words: plan at the start
  - aspects: with the same brain and giving the right (or better) {tool, information source} => better result
  - planning: goal -> divide -> actions -> implement a task (conquer) -> feedback -> update plan
  - progress: ad hoc(no planning at all) -> planning -> {fixed planning -> adaptive planning}
- [ ] 03. The Capability Architectural Pattern
- [ ] 04. Ahead of Time Planning for Improving Agent Reasoning
- [ ] 05. Improving AI Agent Reasoning with In-loop Planning
- [ ] 06. Intermediate Planning: Tracking Progress in the Agent Loop
- [ ] 07. The Great Agent Trade-off: Ahead of Time vs. Dynamic
