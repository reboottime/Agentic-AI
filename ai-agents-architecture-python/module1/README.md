# Extending AI Agents with Self-Prompting

- A persona  
  - is armed with tools
  - has its role in a context. You can see more on the `persona pattern` in notes section.
  - a tool can also be a pers

> The persona pattern represents one of the most powerful and efficient abstractions in prompt engineering. When we invoke a persona, we’re not simply providing a collection of static rules or facts - we’re activating a complex, integrated reasoning system that the LLM has internalized through its training.

## Progress

- [x] Prompts as Computation
- [x] Self-Prompting & Clean Separation of AI Agent Reasoning  
- [x] Bridging Computer Tools & Unstructured Data with Prompting - the AI Shim
- [x] AI Agent Structured Data Extraction
- [x] An Invoice Processing Agent
- [x] The Persona Pattern and Reasoning - Personas are an efficient programming abstraction
- [x] The Persona Pattern  
- [x] Format of the Persona Pattern
- [x] Simple Multi-Agent Systems with Personas
- [x] Consulting Experts or Simulating with the Persona Pattern
- [ ] The Persona Abstraction & Agents: The Persona as an Agent Building Block
- [x] Invoice Processing with Experts
- [ ] Using Human Policies for Document-as-Implementation
- [ ] Persona & Self-Prompting Review

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
- [x] Simple Multiple-Agent Systems with Personas
  - keywords: `action`, `goals`. `At each step, you output must be an action to take`
  - example
  
    ```markdown

    I'd like to simulate an Al agent that I'm designing. The agent willbe built these components:

    Goals: Document all of the code in the project 
    Actions:
        - get_project_directory()
        - list_files(fully_qualified_path)-read _file(fully_qualified _path)
        - ask_documentation_expert_to_write_readme(file_content)- write file(fully_qualified _path, string_contents)

    At each step, your output must be an action to take.
    Stop and wait and l will type in the result of the action as my next message.
    Ask me for the first task to perform.
    ```

- [x] [The Persona Abstraction & Agents](./11.The%20Persona%20Abstraction%20&%20Agents%20_%20Coursera.pdf)
  - [x] Notes:
    - The Persona as an Agent Building Block
      - Why this method works well:
        - activates an extensive cognitive framework that includes: Implicit Domain Knowledge, Methodological Understanding, Contextual Adaptation, Integrated Value Systems.
        - The persona abstraction works because LLMs have been trained on vast amounts of text that demonstrate how different types of experts think, communicate, and reason. **Learn from the master**
      - Prompt guide from above perspectives: Be Specific But Concise,Leverage Established Roles, **Enhance Rather Than Override**, and Test for Activation.
      - Mindset shift: The persona pattern represents a fundamental shift in how we conceptualize knowledge within agent systems. Rather than treating expertise as a monolithic entity that must be encoded entirely within an agent's core prompt, this pattern treats specialized knowledge as a modular resource that can be defined, maintained, and invoked independently.
    - Expertise as a Modular Resource
    - [Metacognition](https://en.wikipedia.org/wiki/Metacognition) Through Role-Switching: By having the LLM adopt different personas, the system can approach problems from multiple cognitive frameworks, each with its own set of priorities, assumptions, and methodologies.
    - Dynamic vs. Static Expertise
      - Static Expertise :Pre-defined Persona Tools
      - Dynamic Expertise: On-the-fly Persona Creation. A persona expert creates needed person dynamically, see the [solution here](./toolsets.py)
  - [x] Recap
    - [x] why
      - The Persona as an Agent Building Block
        - boosts resource efficiency (information is compressed by persona) and capability effectiveness(persona based cognitive framework)
        - supports integrate with multiple personas then multiple perspectives -> avoid cognitive problems (bias and conflicts)
        - support chain of expertise
        - brings better modularity and maintainability in artifacts
        - **better deterministic**
    - [x] how
      - prompt engineering: e Specific But Concise, leverage established roles, enhance rather than override then test persona Activation with preliminary questions
      - solution code:
        - [consult persona expert to get persona profile](./codebase.md#consult-persona-expert-to-get-persona-profile). Find expert through expertise domain and problem description -> get reply from that expert
        - [example of chain of expertise](./codebase.md#chain-of-expertise-example)
