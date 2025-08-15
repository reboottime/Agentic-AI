# Extending AI Agents with Self-Prompting

- [Prompts as computation](https://www.coursera.org/learn/ai-agents-architecture-python/lecture/9Nhwf/prompts-as-computation):

  - > Think about generative AI itself and prompts as a new form of computation. I want you to start thinking of prompts themselves as computation because when you start thinking of prompts as computation, that means you can start building tools for your agent that are based on prompts that you create.
  - Questions?:
    - [ ] Would we think about role first?
    - [ ] Would their role define the prompt then define the tools?
- Self-Prompting & Clean Separation of AI Agent Reasoning
  - > **Clean Architecture**: [The agent's primary job is to coordinate actions and achieve goals, not to become entangled in domain specific reasoning. Hence, we need to maintain a clear separation between the agent's  strategic thinking and the specialized analytical capabilities](./self-prompting-agents.md#the-challenge-of-clean-architecture)
    - Understand using analogy: A CEO doesn't need to be an expert in any domain but knows when to ask who and coordinate their inputs toward company goals.
    - [ ] The solution is to isolate these prompts that are focused on a specific tasks and expose them as tools.
  - self dialog:  **When we expose “prompting” as a tool to the agent** (Interesting view), we are allowing it to engage in “self-dialog”. Essentially, it is using its own capabilities to prompt itself for specialized tasks.
  - **The tool based solution**: We can achieve this balance by exposing the LLM's capabilities as tools (see [the how on Udemy using openai agentic python SDK](https://www.udemy.com/course/the-complete-agentic-ai-engineering-course/learn/lecture/49820447#overview). This method helps us
    - Keep the **agent's decision-making process ** clean and focused on coordinating actions
    - Access the full power of LLM-based analysis and transformation when needed
    - Maintain clear boundaries between strategic coordination and specialized processing
    - Create reusable, well-defined interfaces for common analytical tasks