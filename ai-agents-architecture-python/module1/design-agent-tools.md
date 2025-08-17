# Tool Design Principles

## More Comprehensive Statement

```markdown
Tool design principles: **single responsibility, proper error handling, clear interfaces, and composability**. These align with general software engineering best practices but with **additional considerations for AI agent systems**.
```

## Why the Expanded Version is Better

### Beyond General Programming

While similar to general programming, AI agent tools have **unique requirements**:

- **Deterministic outputs** for reliable agent decision-making
- **Structured error responses** that agents can interpret
- **Context awareness** through ActionContext parameters  
- **Metadata-driven discovery** via tags and schemas
- **Stateless design** for parallel execution safety

### Core Design Principles

1. **Single Responsibility** - Each tool has one clear purpose
2. **Proper Error Handling** - Structured exceptions and validation
3. **Clear Interfaces** - Type hints and schema validation
4. **Composability** - Tools can be chained and combined
5. **Idempotency** - Same inputs produce same outputs
6. **Context Passing** - ActionContext enables coordination

### Agent-Specific Considerations

```python
@register_tool(tags=["data_processing"])
def process_data(action_context: ActionContext, data: str) -> dict:
    """
    AI-friendly tool design:
    - Clear input/output types
    - Structured error responses  
    - Metadata for agent selection
    - Context for coordination
    """
```
