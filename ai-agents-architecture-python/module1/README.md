# Extending AI Agents with Self-Prompting

A person who is

- armed with its tools
- has its role in a context. You can see more on the `persona pattern` in notes section.

## Progress

- [x] **Prompts as Computation**
- [x] **Self-Prompting & Clean Separation of AI Agent Reasoning**  
- [x] **Bridging Computer Tools & Unstructured Data with Prompting - the AI Shim**
- [x] **AI Agent Structured Data Extraction**
- [x] **An Invoice Processing Agent**
- [x] **The Persona Pattern and Reasoning - Personas are an efficient programming abstraction**
- [x] **The Persona Pattern**  
- [x] **Format of the Persona Pattern**
- [x] **Simple Multi-Agent Systems with Personas**
- [x] **Consulting Experts or Simulating with the Persona Pattern**
- [ ] **The Persona Abstraction & Agents**
- [x] **Invoice Processing with Experts**
- [ ] **Using Human Policies for Document-as-Implementation**
- [ ] **Persona & Self-Prompting Review**

## Address knowledge Gap

- [ ] [`register_tool`](./register-tool.md)
- [ ] [Principles in design Agent Tool](./design-agent-tools.md)
- [ ] Should we apply the tool design principle when designing an Agent?

## Learnings

- expectation control: each small practical lesson (the reading material with code) takes me about 30 minutes

## Notes

- [Prompts as computation](https://www.coursera.org/learn/ai-agents-architecture-python/lecture/9Nhwf/prompts-as-computation):

  - > Think about generative AI itself and prompts as a new form of computation. I want you to start thinking of prompts themselves as computation because when you start thinking of prompts as computation, that means you can start building tools for your agent that are based on prompts that you create.
  - Questions?:
    - [x] Would we think about role first?
    - [x] Would their role define the prompt then define the tools?
  - Answer: yes it is. The lecturer did not present well. **more accurately, the persona defined by the prompt is the computation block**
- Self-Prompting & Clean Separation of AI Agent Reasoning
- [Agents bridge the gap between unstructured real-world data and computing systems that require structured data](https://www.coursera.org/learn/ai-agents-architecture-python/lecture/e6ijz/bridging-computer-tools-unstructured-data-with-prompting-the-ai-shim). It makes senses to think that prompts as a computation as a prompt (with the help of LLMs) can convert unstructured real world data into structured data.
  - > **Clean Architecture**: [The agent's primary job is to coordinate actions and achieve goals, not to become entangled in domain specific reasoning. Hence, we need to maintain a clear separation between the agent's  strategic thinking and the specialized analytical capabilities](./self-prompting-agents.md#the-challenge-of-clean-architecture)
    - Understand using analogy: A CEO doesn't need to be an expert in any domain but knows when to ask who and coordinate their inputs toward company goals.
    - [x] The solution is to isolate these prompts that are focused on a specific tasks and expose them as tools.
  - self dialog:  **When we expose “prompting” as a tool to the agent** (Interesting view), we are allowing it to engage in “self-dialog”. Essentially, it is using its own capabilities to prompt itself for specialized tasks. (This idea is based on the persona as well)
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
  - Tool design principles: **single responsibility, proper error handling, clear interfaces, and composability**. These align with general software engineering best practices but with **additional considerations for AI agent systems**.
  - [benefits about extracting tools](./05.An_Invoice_Processing_Agent%20_Coursera.md):
    - Cognitive Perspective: less cognitive burden for human being and the agent
    - Code Practice Perspective: better code Maintainability and Adaptability
    - build modular, adaptable systems that grow through the addition of specialized tools.
    > 主帅有谋目标明确，单兵精干可插拔。队伍精干可灵活应变。
- [x] [The persona pattern](https://www.coursera.org/learn/ai-agents-architecture-python/lecture/glo9H/the-persona-pattern-and-reasoning-personas-are-an-efficient-programming)
  - > Pattern: Act as <Persona_Name> whenever you produce an output, produce the outputs that persona would produce.
  - Definition: A programming abstraction that assigns the AI a specific role or identity (e.g., "act as a speech-language pathologist").
  - > Pattern: Act as <Persona_Name> whenever you produce an output, produce the outputs that persona would produce.
  - > In real world, you don't know how the person you ask for help works, but you know who you will ask for help!
  - LLM understands a persona with aspects below:
    - Domain knowledge - What that persona knows
    - Operational capabilities - What that persona does
    - Behavioral patterns - How that persona acts
  - Benefits
    - Implicit Operation Bundling: The persona automatically brings relevant operations without explicit instruction
    - Instead of writing extensive rules and instructions, a few tokens ("act as X") activate comprehensive behavioral patterns the model already understands from training data.
