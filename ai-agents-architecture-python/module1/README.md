# Extending AI Agents with Self-Prompting

## Progress

- [x] **Prompts as Computation**
- [x] **Self-Prompting & Clean Separation of AI Agent Reasoning**  
- [x] **Bridging Computer Tools & Unstructured Data with Prompting - the AI Shim**
- [x] **AI Agent Structured Data Extraction**
- [x] **An Invoice Processing Agent**

- [ ] **The Persona Pattern and Reasoning - Personas are an efficient programming abstraction**
- [ ] **The Persona Pattern**  
- [ ] **Format of the Persona Pattern**
- [ ] **Simple Multi-Agent Systems with Personas**
- [ ] **Consulting Experts or Simulating with the Persona Pattern**
- [ ] **The Persona Abstraction & Agents**
- [ ] **Invoice Processing with Experts**
- [ ] **Using Human Policies for Document-as-Implementation**
- [ ] **Persona & Self-Prompting Review**

### Address knowledge Gap

- [ ] [`register_tool`](./register-tool.md)

## Notes

- [Prompts as computation](https://www.coursera.org/learn/ai-agents-architecture-python/lecture/9Nhwf/prompts-as-computation):

  - > Think about generative AI itself and prompts as a new form of computation. I want you to start thinking of prompts themselves as computation because when you start thinking of prompts as computation, that means you can start building tools for your agent that are based on prompts that you create.
  - Questions?:
    - [ ] Would we think about role first?
    - [ ] Would their role define the prompt then define the tools?
- Self-Prompting & Clean Separation of AI Agent Reasoning
- [Agents bridge the gap between unstructured real-world data and computing systems that require structured data](https://www.coursera.org/learn/ai-agents-architecture-python/lecture/e6ijz/bridging-computer-tools-unstructured-data-with-prompting-the-ai-shim). It makes senses to think that prompts as a computation as a prompt (with the help of LLMs) can convert unstructured real world data into structured data.
  - > **Clean Architecture**: [The agent's primary job is to coordinate actions and achieve goals, not to become entangled in domain specific reasoning. Hence, we need to maintain a clear separation between the agent's  strategic thinking and the specialized analytical capabilities](./self-prompting-agents.md#the-challenge-of-clean-architecture)
    - Understand using analogy: A CEO doesn't need to be an expert in any domain but knows when to ask who and coordinate their inputs toward company goals.
    - [ ] The solution is to isolate these prompts that are focused on a specific tasks and expose them as tools.
  - self dialog:  **When we expose “prompting” as a tool to the agent** (Interesting view), we are allowing it to engage in “self-dialog”. Essentially, it is using its own capabilities to prompt itself for specialized tasks.
  - **The tool based solution**: We can achieve this balance by exposing the LLM's capabilities as tools  (see[convert agents into tools using OpenAI AgenticAI Python SDK on Udemy](https://www.udemy.com/course/the-complete-agentic-ai-engineering-course/learn/lecture/49820447#overview)). This method helps us
    - Keep the **agent's decision-making process** clean and focused on coordinating actions
    - Access the full power of LLM-based analysis and transformation when needed
    - Maintain clear boundaries between strategic coordination and specialized processing
    - Create reusable, well-defined interfaces for common analytical tasks
  - [AI agent structured data extraction](./04.AI%20Agent%20Structured%20Data%20Extraction.md)
    - How
      - [ ] At the first example, why do we ask LLM to give json file in markdown?
      - [ ] `action_context` (I see this in `[Openai Agentic AI Python SDK](https://openai.github.io/openai-agents-python/)`)
    - Classic tradeoff: Flexibility and reliability
      - [x] How the upgraded solution provides better guarantees?
        - improved json schema design
          - required fields
          - field validation
        - improved prompts
- [x] **An Invoice Processing Agent**