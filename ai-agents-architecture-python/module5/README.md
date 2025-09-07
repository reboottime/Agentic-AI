# Module 5: Approaches to Improving AI Agent Reasoning

## Progress

- [x] 01. Improving AI Agent Reasoning with In-Context Learning
  - what is it: show LLMs **correct examples** how to solve a task.
  - rationale:
  - in context learning template:
    - example template
      > - problem
      > - thought
      > - tool(s)
      > - result
    - problem to solve template
      > - problem: problem statement
      > - thought: (blank, expect llm to fill or we fill it)
      > - tools: (blank, expect llm to fill)
      > - result: (blank, expect llm to fill)
  - LLMs are trained to predict the next word
  - showing examples helps llm to **inference** the implicit information and learn pattern(s)
  - The examples listed in the prompt show LLM the pattern it should follow / learn
    - Show agents examples of problems being solved correctly
    - Like training interns by demonstrating the thought process
    - Agent learns patterns from seeing successful executions
  - performance: it is incredibly powerful for agents
- [x] 02. Improving AI Agent Reasoning with Up-front Planning & Chain of Thought.
    > but often it can be really effective if we have it think about plans up front.
  - to improve understanding, first visit [this diagram](http://raw.githubusercontent.com/reboottime/ML-in-LLM-Era/refs/heads/main/courses/Introduction%20to%20Generative%20AI%202024/notes/screenshots/angent.png) to understand how Agent works, then visit [this example](./02.upfront-planning-example.md) to compare the difference between reasoning with ad hoc approach and with upfront planing approach.
  - magic words: plan at the start, think step by step
    - hence, before the agent takes any actions or does any executions, it begins with making a plan.
  - aspects: with the same brain and giving the right (or better) {tool, information source} => better result
  - planning: goal -> divide -> actions -> implement a task (conquer) -> feedback -> update plan
  - progress: ad hoc(no planning at all) -> planning -> {fixed planning & execution -> adaptive planning & execution}
  - model optimization strategy  => balance the planning and execution efficiency
    - higher quality (usually more expensive and slower) model for initial planning (design strategy)
    - use lower quality (usually faster and cheaper) for plan execution
    - separate planning as a tool
- [ ] 03. The Capability Architectural Pattern
  - [ ] What's the difference between `Tools` and `Capabilities` from both
    - [ ] conceptual level
    - [ ] and code organization level
- [ ] 04. Ahead of Time Planning for Improving Initial Plan Generation
  - use a cheaper model for execution
  - iterate the initial plan based on the agent's reasoning
- [ ] 05. Improving AI Agent Reasoning with In-loop Planning
- [ ] 06. Intermediate Planning: Tracking Progress in the Agent Loop
- [ ] 07. The Great Agent Trade-off: Ahead of Time vs. Dynamic
