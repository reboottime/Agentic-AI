# Persona & Self-Prompting Review

## Quiz List

- Quiz 1:
  - Q: why Personas are an efficient prompting abstraction.
  - A: The efficiency comes from two aspects: cost and performance
    - performance:
      - During the pre-training and fine-tuning stages, LLMs learn cognitive frameworks of various personas. When a persona is specified in a prompt, it activates the corresponding cognitive framework, which provides access to high-density information including implicit domain knowledge, methodological understanding, context, and integrated value systems.
      - In a prompt, we cannot enumerate all the information that a persona provides using a small amount of tokens.
      - Additionally, the more (yet not accurate) information we provide, the more time LLMs take to reasoning
      - Therefore, personas are an efficient prompting abstraction from a performance perspective.
    - financial cost: both input to LLMs and output from LLMs cost tokens. Currently, LLM service providers charge for services on a token-based pricing model. Since a persona requires fewer tokens than providing detailed explanations of various contexts and rules, using personas reduces token consumption and therefore costs less money.
- Q2:
  - Q: why exposing self-prompting as a tool helps improve modularity, testability, and other properties of the agent versus integrating the prompt directly into the agent reasoning.
  - A: while LLMs are capable working on task in different domains, yet this is not a good implementation strategy. For each input,  LLM generates a series of prediction options with possibilities, then there is a lottery process to select one version, then outputs a response.  the more role the LLM takes, it may confuse it self, the output is less deterministic, hence less testable. Using self-prompting as a tool can make each functional and persona agents more focused and effective.