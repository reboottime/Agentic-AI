# README

**About This Course**: Please visit [OpenAl GPTs: Creating Your OwnCustom Al Assistants](https://www.coursera.org/learn/openai-custom-gpts) to get more information.

**Why this course**: While the topic is about customizing OpenAI GPTs, the content introduced in the lectures contains some fundamental practices:

- Agent persona design, see [note here](https://github.com/reboottime/Agentic-AI/blob/feature/openai-custom-gpts/openai-custom-gpts/persona-architecture.md)
- [x] Agent Evaluation and testing, see module 2, benchmark design related content
- Solve some of my personal assistants needs using OpenAI GPT

## Course Content and My Progress

- [x] Module 1: Custom GPT Fundamentals
  - [x] Welcome (Video)
  - [x] Programming a GPT (Video)
    - prompt: from now on triggers writing memory
    - core ideas:
      - context engineering, providing your information so LLM can work on your case, not a general response
      - it is about preparing for the future
  - [x] Custom Instructions (Video)
    - why:
      - ensure every conversation incorporates this background information [system prompt]
      - even a conversation gets very long, the core background information is still in LLM's mind
      - instruction can change LLM behaviors
    - core questions:
    - terms
      - **guardrails**: how to preset some rules that users can't easily change it, to limit what can or can not be done
      - context(background) What would you like ChatGPT to know about you to provide better responses? [context]
      - rules: How would you like ChatGPT to respond? [style]. For example:
      > Always respond concept in a fun way that I can understand and wave my interest
  - [x] Retrieval Augmented Generation (RAG) (Video)
    - how it benefits you:
      - LLMs are trained on data that are cut off by its time. Hence, LLMs don't have idea about facts & informations that are not in its training data
      - Providing Information after its training cut off time that it doesn't know
    - what is it:
      - simplified version:
         <img src="https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Frag-framework.81dc2cdc.png&w=3840&q=75" width="480" alt="RAG Framework" />
         *Source: [promptingguide.ai/research/rag](https://www.promptingguide.ai/research/rag)*
      - detailed version:
          <img src="./module01/topics/imgs/rag.png" width="480" alt="RAG Detailed Framework" />
          *Source: [codingscape.com/blog/rag-101-what-is-rag-and-why-does-it-matter](https://codingscape.com/blog/rag-101-what-is-rag-and-why-does-it-matter)*
    - practices:
      - Also give instructions to situations where there are multiple resources, which one do you preference and how do you use different piece of information
  - [x] Putting it All Together: Custom GPTs (Video)
    - Findings: You can create a GPT and only for your own usage
    - [x] questions: Answered in the tools lecture
      - how can fetch data from my own private source
        - source
        - authentication
      - how to retrieve user data from remote?
      - how to do payment integration?
  - [x] Understanding How GPTs Use Tools (Video)
    - what it is about: your own customized tools description
      - [x] Read actions documentation: Let your GPT retrieve information or take actions outside of ChatGPT. See how to add actions from [OpenAI documentation here](https://platform.openai.com/docs/actions/introduction)
      - Only introduce actions when needed, as adding actions also introduces complexity to GPT
  - [x] CAPITAL: A Framework for Customizing How Chatbots Converse (Reading)
    - What is it?: **The CAPITAL framework is a comprehensive guide used to customize the interaction style of a GPT, ensuring it communicates effectively with its intended audience.**
    - [x] How to make GPT follow the *CAPITAL* framework?. The answer, building a persona for your GPT with customized characteristics
  - [x] Building a Persona for Your Custom GPT (Video)
    - thought process:
      - who would be the ideal person to help you process the task? what traits would you want the person has?
      - ask GPT to tell you who would be the person can help you then get the persona
    - what is it
      - find the persona for our GPT
      - and add some characteristic
  - [x] Prompt Patterns (Reading)
  - [x] Format of the Persona Pattern (Reading)
    - template:
      - Act as Persona X
      - Perform task Y
    - examples:
      - > Act as a speech language pathologist. Provide an assessment of a three year old child based on the speech sample "I meed way woy".
      - > Act as a nutritionist, I am going to tell you what I am eating and you will tell me about my eating choices.
  - [x] Create a GPT Persona (Graded Assignment)
  - [x] Learning More & Staying Connected (Reading)

- [x] Module 2: THINK: Create Great GPTs (Part I). User Experiences
  - [x] Test (Video): what we need: create a benchmark to evaluate & test how well the GPT is doing.
  - [x] Build a Benchmark (Video)
  - [x] Benchmark Design Considerations ([Reading: Benchmark Design Considerations](./module02/topics/Benchmark%20Design%20Considerations.pdf))
  - [x] Build a Custom GPT for Generating Test Cases
    - LLM challenges LLM. help you brainstorming and broad the perspectives in evaluation cases
    - [x] Questions:
      - could the evals be built by the domain expert
      - or a combination of both domain expert and evals expert
    - To view the template the lecturer presented, pls click [here](./module02/topics/test-gpt-conf.md)
    - Rubric: The rubric provides a structured scoring system to assess how well the custom GPT performs on each specific test case. It establishes clear criteria for what constitutes good vs. poor performance.
  - [x] Build Your Own Custom GPT Test Case Generator (Graded Assignment)
  - [x] The Goal is to Help the Human Solve the Problem, Not Provide the Answer (Video)
    - To augment human, not to replace human. Help human think better and not think less or poorer
  - [x] How to Cite Knowledge (Video)
    - why providing citation from docs:
      - two points:
        - to help user understand why
        - and minimize the risk that you get wrong
      - as generative ai is the source of facts. You can get more understanding from [Trustworthy Generative AI](https://www.coursera.org/learn/trustworthy-generative-ai/)
    - the point is to help user reasoning, not replacing their reasoning capabilities
  - [x] Output Formatting (Video)
    - template
      - in the following format:
      - <content>...(can have more)
  - [x] Template Pattern & Markdown (Reading)
  - [x] Provide the Facts (Video)
  - [x] Hedging While Helping (Video). Pre bake a bunch of options that user might need
  - [x] Menu Action Pattern (Video)
  - [x] Format of the Menu Actions Pattern (Reading)
  - [x] Where to Get Additional Help (Video)
  - [x] Building a GPT with a Menu (Graded Assignment)
  - problem solving process
    - [x] Information Before Decision Making (Video)
    - why:  Generative AI always wants to try to solve the problem, and this leads to hallucination. so we instruct our GPTs to ask  users information until it reaches a threshold of understanding to problem, then solve the problem. This follows the process of *[How to solve it](https://en.wikipedia.org/wiki/How_to_Solve_It)* problem solving process
    ![x](./module02/topics/4steps-problem-solving.png)
    - [x] Flipped Interaction Pattern (Video)
      - ask user questions to understand and scope the problem
    - [x] Format of the Flipped Interaction Pattern (Reading)
    - [x] Missing Context from the User (Video). Who is the user, personalization
  - [x] User-Customized Experiences (Video)
  - [x] A Personalized GPT (Graded Assignment)

- [ ] Module 3: THINK: Create Great GPTs (Part II)
  - [ ] Boundaries (Video)
  - [ ] How to Respond to the Absence of Knowledge (Video)
  - [ ] Combating Ambiguity in User Prompts with Question Refinement (Video)
  - [ ] Format of the Question Refinement Pattern (Reading)
  - [ ] Enforcing Boundaries & Still Helping with the Alternative Approaches Pattern (Video)
  - [ ] Format of the Alternative Approaches Pattern (Reading)
  - [ ] Cognitive Verifier Pattern (Video)
  - [ ] Format of the Cognitive Verifier Pattern (Reading)
  - [ ] Applying Patterns (Graded Assignment)
  - [ ] Handling Ambiguity in Concept Mapping (Video)
  - [ ] Knowledge Conflict Resolution (Video)
  - [ ] You and Your Business are Responsible, Not the Bot (Video)
  - [ ] Adversarial Testing (Video)
  - [ ] Wrapping Up (Video)
  
## Discoveries

- How context engineering
- How to get around the guardrails
- [persona architecture](./persona-architecture.md)
