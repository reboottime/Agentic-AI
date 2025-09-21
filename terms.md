# Terms

- [agent persona](https://youtu.be/W2HVdB4Jbjs?si=Tye2oaQGw0qXI-gC&t=603), see 2
  - Description: Stores agent identity information, including personality traits, roles, expertise domains, and communication styles
  - Contents: Name, role, goals, background, and vector embeddings for semantic retrieval
  - Usage: Provides consistent identity for agents across interactions and sessions
  - Schema: Includes persona_id, name, role, goals, background fields with embedding vectors
- [toolbox for agent](https://youtu.be/W2HVdB4Jbjs?si=3bmEwdJgCzvKpQEq&t=662)
  - Description: Stores tool definitions, metadata, parameter schemas, and embeddings for function capabilities
  - Contents: Tool names, descriptions, parameter specifications, and vector embeddings
  - Usage: Enables semantic discovery and execution of external functions by agents
  - Schema: Includes tool_id, name, function metadata, parameters, and embedding vectors
- [**Embedding models**](http://docs.voyageai.com/docs/introduction) are neural net models (e.g., transformers) that convert unstructured and complex data, such as documents, images, audios, videos, or tabular data, into dense numerical vectors (i.e. embeddings) that capture their semantic meanings, see 1.
- evals: evaluate your llms or ai system. It also means the [evals python framework built by openai](https://github.com/openai/evals). Learn practices about evals, see 1,2,3
- agentic loop: An agentic loop is a continuous, iterative cycle where an AI agent perceives its environment, reasons through a problem, takes an action, and then evaluates the result through feedback. see [reference 3](https://youtu.be/WJjInLeaJjo?si=GiHIHkE9AOp0ba-S&t=511) to see the agentic loop diagram

## References

- 1. [Five hard earned lessons about Evals — Ankur Goyal, Braintrust](https://www.youtube.com/watch?v=a4BV0gGmXgA&list=PLcfpQ4tk2k0W3ORTR-Cr4Ppw6UrN8kfMh&index=3)
- 2. [Evals Are Not Unit Tests — Ido Pesok, Vercel v0](https://www.youtube.com/watch?v=L8OoYeDI_ls&list=PLcfpQ4tk2k0W3ORTR-Cr4Ppw6UrN8kfMh&index=16)
- 3. [2025 is the Year of Evals! Just like 2024, and 2023, and … — John Dickerson, CEO Mozilla AI](https://www.youtube.com/watch?v=CQGuvf6gSrM&list=PLcfpQ4tk2k0W3ORTR-Cr4Ppw6UrN8kfMh&index=17)
- 4. [Building Agents at Cloud Scale — Antje Barth, AWS](https://youtu.be/WJjInLeaJjo?si=GiHIHkE9AOp0ba-S&t=511). The presenter has a book [Generative AI on AWS: Building Context-Aware Multimodal Reasoning Applications ](https://www.amazon.com/Generative-AWS-Context-Aware-Multimodal-Applications/dp/1098159225)