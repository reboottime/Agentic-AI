# Multiple Agent Systems

## Progress

- [x] 00. Introduction to Multi-Agent Systems: brain, coordination and share information
- [x] 01. Building Multi-Agent Systems: Agent-to-Agent Communication
  - [x] [how agent registry and action context works](./codebase.md#how-to-do-agent-discovery)
- [x] 02. Agent Interaction & Memory
- [x] 03. [Agent Interaction Patterns with Memory](./03.agent-interaction-and-memory.md)
  - [x] Solutions:
    - Message passing mode
    - Shared Memory Model
  - [x] decision tree: Choose coordination approaches based on task complexity, required isolation, and context needs.
- [x] Agent interaction patterns with memory.
  - [x] Message Passing: The Basic Pattern
  - [x] Memory Reflection: Learning from the Process. For example, if a research coordinator agent asks a data analysis agent to study some results, seeing the analysis process helps the coordinator better understand and use the conclusions.
  - [x] Memory Handoff: Continuing the Conversation: This is like having a colleague step in to take over a project - for example, the customer support agents hands off the task to a tech support agent with the problem description.
- [x] 05. Removing Noise: Focusing Agent Attention
  - constraints
    - output token is more expensive than input
    - LLM usually can take more in than output
  - solutions pros and cons
    - options:
      - extract relevant task info
      - or output memory task
    - pros and cons
      - Hallucination Prevention - Agents can only reference existing memory without modifying content, cannot summarize or rewrite original information, and protects data integrity especially for API query results.
      - Specialized Selection - Enables designing dedicated "selector" agents specialized in identifying relevant memory fragments, reducing burden on the main agent.
      - Scalable Processing - The second agent can receive large amounts of context information, exceeding the first agent's output limitations and fully utilizing input token capacity.
- [x] 06. Advanced Agent Interaction
- [ ] 07. Providing Agentic AI Information About the World
- [ ] 08. Agent Interaction Architectures
