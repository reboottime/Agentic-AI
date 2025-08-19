# Multiple Agent System

Q: write 2-3 paragraphs discussing the key patterns for agent interaction and when you might want to use each.
A: There are four key agent interaction patterns that enable effective multi-agent collaboration:

## The Four Agent Interaction Patterns

1. **Message Passing**
   - Keeps interactions simple and focused
   - When to use: When the task is simple and straightforward

2. **Memory Reflection** 
   - Helps agents learn from each other's processes
   - When to use: When the caller agent wants to learn how the downstream agent reached the conclusion
   - Example: Chief research scientist learning from a research scientist's analysis process

3. **Memory Handoff**
   - Enables seamless continuation of complex tasks
   - When to use: When the called agent needs the full context information to process the delegated task
   - Example: Tech support agent needs the whole context about customer's complaint

4. **Selective Memory Sharing**
   - Provides relevant context while reducing noise
   - When to use: When you need to filter out unnecessary or sensitive information
   - Example: In customer support scenarios, avoid conveying customer ID validity process memory to tech support agents to:
     - Prevent information overload that could confuse the agent
     - Address security concerns about identity information leaks