# AI Agent Best Practices

## Async/Await with AI Agents

### When to Use Async/Await

- **Network I/O operations**: API calls to LLM providers (OpenAI, Anthropic, etc.)
- **File I/O operations**: Reading/writing large files
- **Database operations**: Queries that might take time
- **Any operation that waits**: Network requests, external services

### Simple Async Pattern

```python
import asyncio

async def main():
    agent = AIAgent(model, api_key, system_prompt)
    response = await agent.get_response("Hello")
    print(response)

# Run the async function
asyncio.run(main())
```

### Benefits of Async for AI Agents

1. **Non-blocking**: Your program doesn't freeze during API calls
2. **Concurrent requests**: Can handle multiple conversations
3. **Better UX**: Responsive applications
4. **Resource efficient**: No thread blocking

### Session Management (Advanced)

- **Simple approach**: Let libraries (like `litellm`) handle sessions internally
- **Advanced approach**: Use `aiohttp.ClientSession` for custom HTTP management
- **When to learn**: After mastering basic async patterns

### Common Patterns

#### Single Agent Interaction

```python
async def chat_with_agent():
    agent = AIAgent(model, api_key, prompt)
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
            
        response = await agent.get_response(user_input)
        print(f"Agent: {response}")

asyncio.run(chat_with_agent())
```

#### Multiple Concurrent Agents

```python
async def run_multiple_agents():
    agents = [
        AIAgent(model, api_key, "You are a helpful assistant"),
        AIAgent(model, api_key, "You are a creative writer"),
        AIAgent(model, api_key, "You are a code reviewer")
    ]
    
    tasks = [
        agent.get_response("Hello") 
        for agent in agents
    ]
    
    responses = await asyncio.gather(*tasks)
    for i, response in enumerate(responses):
        print(f"Agent {i+1}: {response}")

asyncio.run(run_multiple_agents())
```

### Key Takeaways

1. Start simple with `asyncio.run()`
2. Use `async def` for functions that call LLM APIs
3. Use `await` for LLM API calls
4. Learn advanced session management later
5. Focus on the async pattern first, optimize later
