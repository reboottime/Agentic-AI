# Code Samples

## How LLM (for example Claude) terminates its thought if you asked a question makes it loop

```python
# The Agent Loop
while iterations < max_iterations:

    # 1. Construct prompt: Combine agent rules with memory
    prompt = agent_rules + memory

    # 2. Generate response from LLM
    print("Agent thinking...")
    response = generate_response(prompt)
    print(f"Agent response: {response}")

    # 3. Parse response to determine action
    action = parse_action(response)

    result = "Action executed"

    if action["tool_name"] == "list_files":
        result = {"result":list_files()}
    elif action["tool_name"] == "read_file":
        result = {"result":read_file(action["args"]["file_name"])}
    elif action["tool_name"] == "error":
        result = {"error":action["args"]["message"]}
    elif action["tool_name"] == "terminate":
        print(action["args"]["message"])
        break
    else:
        result = {"error":"Unknown action: "+action["tool_name"]}

    print(f"Action result: {result}")

    # 5. Update memory with response and results
    memory.extend([
        {"role": "assistant", "content": response},
        {"role": "user", "content": json.dumps(result)}
    ])

    # 6. Check termination condition
    if action["tool_name"] == "terminate":
        break

    iterations += 1

```
