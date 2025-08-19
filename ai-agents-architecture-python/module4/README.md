# Module 4: Dependency Injection for Tools

## Progress

- [x] 01. Isolating Agents from Accidental Complexity: move complexity to tool using dependency injection
- [ ] 02. Clean AI Tools with Dependency Injection  
  - how 
    - the action_context helped me. This resolved my confusion about why OpenAi Agentic AI Python SDK uses `context.context`
    - we have our ActionContext to hold shared resources and dependencies,
  - [member methods on python dictionary](https://www.geeksforgeeks.org/python/python-dictionary-methods/)
  - tool built on top of LLM reads it needed memory from action context
  - [x] when the `should_terminate` is marked as true in the [`Handling Session or Request-Specific Dependencies`](./03.clean-tool-dependency-injection-with-the-environment.md#handling-session-or-request-specific-dependencies) code sample? I see, it depends on LLM to make the judgement in the code sample case.
- [ ] 03. Clean Tool Dependency Injection with the Environment
  