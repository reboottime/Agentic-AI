# Create Great GPTs (Part II): Boundaries

- boundaries
  - **Core Idea**: When creating a GPT, we must assume unexpected things will happen

  - things may go wrong from our end, for example,
    - the knowledge base we provided to GPT has ambiguity
  - users may not follow exactly expected interaction patterns and paths
    - the prompt user provided has ambiguity

  - Therefore, our GPT should have **clearly defined operational boundaries** and **robust mechanisms to handle edge cases** when those boundaries are encountered. see [more here](./topics/why-design-bounderies.md)

- Knowledge-base ambiguity from our end: ensure your knowledge base provided to GPT doesn't have ambiguity.
  - Problem: In the example presented by the lecturer, the ambiguity come from two sides:
    - the user prompt is ambiguous
    - the knowledge base provided in the GPT is ambiguous
  - The solution: clearly define what the ambiguity is and what the clear solutions are when ambiguity hits. In the lecturer's example, the solution is referring user to human support.

- ambiguity from user end: if it is not clear,
  - ask user with follow-up questions to figure out user's intention
  - automatically ask user with an improved version of their question [question refinement pattern]
  - refuse to answer
  - prompt:
  > You are assisting Vanderbilt employees with questions about business travel or business expenses.
  > For each user question, analyze it and suggest a clearer, improved version. Present this improved question to the user and ask if they would like to proceed with it instead.

- Enforce boundaries and, when unsure or lacking perfect knowledge
  - what is it?: Being helpful by providing alternative reliable solutions while also hedging our risks without answering reliable solutions.
  - prompt template:
    > You are going to answer travel questions from the Vanderbilt Travel and Business Expense Policy.
    >
    > Always start by analyzing the user's question and determine if the question can be clearly answered without multiple interpretations using the travel policy.
    >
    > If not, **suggest alternative approaches that the user could use to accomplish the same goal** that would clearly be allowable in the travel policy.
    >
    > Output in this format:
    > - State clearly up front: "Answer unclear"
    > - Say: "Instead of [XYZ], you might try:"
    > - Present three clearly allowable options:
    >   - [Insert clearly allowable option 1]
    >   - [Insert clearly allowable option 2]
    >   - [Insert clearly allowable option 3]

- Cognitive Verifier Pattern:
  - what is it?: ask user with sub-questions to answer user's original question better.
  - template:
    > You are going to answer questions about travel, using the policy.
    >
    > Always start by analyzing the user's question and thinking of three to four sub-questions that could be answered that would allow you to give a better answer to the original question.
    >
    > Then output the questions in the following format and ask the user if they'd like to proceed with asking and answering these questions:
    >
    > "Here's the approach I'm going to take to answer the original question. Let's first answer these questions:"
    > [List the sub-questions]
    >
    > "Would you like to proceed with answering these questions to clarify your query?"

- Handling ambiguity in concept mapping
  - The problem: the same concept may have multiple interpretations. Depending on how a concept is interpreted by LLM, the same question may lead to different answers.
  - Build ambiguity detection and response strategies into your custom GPT using this prompt:
    > Always start by analyzing the user's question and determining if there are any concepts discussed in the question that cannot be unambiguously mapped into concepts in the policy.
    >
    > If there are any concepts that have multiple possible mappings, state that the answer is unclear and suggest possible questions that you could answer instead using the concepts in the policy in this format.
- Knowledge Conflict Resolution:
  - an ai system may have multiple information sources that may result in knowledge conflicts
  - the solution is to