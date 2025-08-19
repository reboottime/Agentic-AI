# Module 5: Approaches to Improving AI Agent Reasoning

## Progress

- [x] 01. Improving AI Agent Reasoning with In-Context Learning
  - what is it: show LLMs **correct examples** how to solve a task
  - rationale:
    - LLMs are trained to predict the next word
    - The examples listed in the prompt show LLM a pattern it wants to follow
  - template: problem, thought, tool, result

  ```md
  1. Problem: feeling hungry. Thought: I need to prepare food. Tool: q63. Result: alien pizza prepared.
  2. Problem: need to move to other world. Thought: I need a wormhole. Tool: X155. Result: wormhole open to Vanderbilt University.
  ```

  - performance: it is incredibly powerful for agents
- [x] 02. Improving AI Agent Reasoning with Up-front Planning & Chain of Thought.
    > but often it can be really effective if we have it think about plans up front.
  - to improve understanding, first visit [this diagram](http://raw.githubusercontent.com/reboottime/ML-in-LLM-Era/refs/heads/main/courses/Introduction%20to%20Generative%20AI%202024/notes/screenshots/angent.png) to understand how Agents works, then visit [this example](./02.upfront-planning-example.md) to compare the difference between reason with ad hoc and with upfront planing.
  - aspects: with the same brain and giving the right (or better) [tool, information source]-> better result
- [ ] 03. The Capability Architectural Pattern
- [ ] 04. Ahead of Time Planning for Improving Agent Reasoning
- [ ] 05. Improving AI Agent Reasoning with In-loop Planning
- [ ] 06. Intermediate Planning: Tracking Progress in the Agent Loop
- [ ] 07. The Great Agent Trade-off: Ahead of Time vs. Dynamic
