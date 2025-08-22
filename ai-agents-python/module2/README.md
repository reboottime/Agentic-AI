# Module 2: Agent Tools and Function Calling

## Progress

- [x] 01. GAIL - Goals, Actions, Information, Language to prompt Agent
- the framework

 ![x](./topics/imgs/gail-framework.png)

 ![x](./topics/imgs/gail-framework2.png)

- example
   > You are Action Agent, a helpful Al assistant.
    Your goal is to accomplish the task given by the user.
    If you have enough information to directly respond to the user'srequest, you should do so. lf you need to complete tasks, you canuse the provided tools to help you. Whenever you are completelydone with the task, you should tell the user the result and terminatethe conversation.
    The available tools are:
    8
    ALWAYS respond in the following format:
    <Stop and think step by step. Insert a rich description of your step bystep thoughts here.>

        ```action
        {{
        "tool": "tool name"
        "args":fffill in anv reguired arauments here.
        }}
        ```

- [ ] 02. Giving Agents Tools
- [ ] 03. Tool Descriptions and Naming
- [ ] 04. Tool Results and Agent Feedback
- [ ] 05. Agent Tools in Python
- [ ] 06. Try Out an Agent that Calls Python Functions
- [ ] 07. Using Function Calling Capabilities with LLMs
- [ ] 08. Try Out LLM Function Calling
- [ ] 09. An Agent Loop with Function Calling
- [ ] 10. Try Out an Agent Loop with Function Calling
- [ ] 11. Exercise: Extend the Function Calling Agent
- [ ] 12. Agent Tool Design Best Practices
- [ ] 13. Understanding the AI Agent Loop (Graded Assignment)
