# Module 3: GAME Framework and Agent Design

## Progress

- [x] 01. Overview of the GAME Framework:
  - what is it ?: Goal, Action, Memory, Environment.
  - ![x](./topics/imgs/calendar-agent.png)
  - implementation tricks:
    - prototype the agent conversations quickly to identify
    - check [agent.py](./topics/code/angent.py) to view codebase concept design  in Python
- [x] 02. Designing AI Agents with GAME
  - Goal
    - objective - what
    - instructions - how
  - [x] why actions define what the agent can do? not what the agent is gonna todo?
    > For example, an agent might have an action called read_file(), which is simply a placeholder in the Actions layer. The Environment then provides the actual logic, handling file I/O operations and error handling to ensure the action is executed correctly.

  - [x] coding task: `coding_agent.py`
- [x] 03. Simulating Agents in ChatGPT.
- [x] 04. Simulating GAME Agents in Conversation
  - [x]  why?
    - [ ]  workflow wise
      - The goals are achievable with the planned actions
      - The memory requirements are reasonable
      - The actions available are sufficient to solve the problem
      - The agent can make appropriate decisions with the available information
    - Engineering practice
      - The simulation environment provides a safe space to test termination conditions.
      - quick prototyping and iteration
    - Learning from the Age:At the end of your simulation sessions, ask the agent to reflect on its experience. What tools did it wish it had? Were any instructions unclear? Which goals were too vague? The LLM can often provide surprisingly insightful suggestions about how to improve your GAME design.
  - template
      > I'd like to simulate an AI agent that I'm designing. The agent will be built using these components:
      >
      > Goals: [List your goals]
      > Actions: [List available actions]
      >
      > At each step, your output must be an action to take.
      >
      > Stop and wait and I will type in the result of
      > the action as my next message.
      >
      > Ask me for the first task to perform.
- Code Architecture Practice
  - [x] 05. Modular AI Agent Design
    - insights:  GAME Component are what change from none agent to another while core loop stays the same.
    - actions define what agent can do, think of them as the agent's toolkit
    - [ ] [the environment design](./topics/05.modular-ai-agent-design.md#e---environment-implementation) seems strange to the previous `agent.py` practice
  - [ ] 06. Agent Loop Customization
  - [ ] 07. Implementing GAME in Code
  - [ ] 08. Try Out the Agent Framework
  - [ ] 09. How Your Agent Communicates with the LLM: The Agent Language
  - [ ] 10. Putting It All Together: Document Your Code with a README Agent
