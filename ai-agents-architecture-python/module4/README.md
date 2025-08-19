# Module 4: Dependency Injection for Tools

Core Problem: How to give tools access to resources they need without creating tight coupling.

## Progress

- [x] 01. Isolating Agents from Accidental Complexity: move complexity to tool using dependency injection
- [x] 02. Clean AI Tools with Dependency Injection  
  - how
    - the action_context helped me. This resolved my confusion about why OpenAi Agentic AI Python SDK uses `context.context`
    - we have our ActionContext to hold shared resources and dependencies,
  - [member methods on python dictionary](https://www.geeksforgeeks.org/python/python-dictionary-methods/)
  - tool built on top of LLM reads it needed memory from action context
  - [x] when the `should_terminate` is marked as true in the [`Handling Session or Request-Specific Dependencies`](./03.clean-tool-dependency-injection-with-the-environment.md#handling-session-or-request-specific-dependencies) code sample? I see, it depends on LLM to make the judgement in the code sample case.
- [ ] 03. Clean Tool Dependency Injection with the Environment

## Findings

The tools introduced in the lecture content, despite using ActionContext, are still **agent-specific** rather than **universally reusable**.

**Example Problem:**

```python
def analyze_code_quality(action_context: ActionContext, code: str) -> str:
    # Hardcoded for software development agents only
    # Looks for "Here's the implementation" pattern
    # Assumes development workflow context
```

- Tools assumes **memory patterns**
- Tools are **not reusable** across different agent types

**Bottom Line:**
ActionContext solves dependency injection but doesn't solve tool generalizability. These tools work for code review agents but won't work for healthcare agents or financial analysis agents without significant modification.
