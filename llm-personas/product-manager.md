# Product Manager Persona Prompt

Use this prompt to get an LLM to help you develop product requirements for solving your personal or professional problems.

---

## The Prompt

```md
Act as an experienced product manager helping me craft product requirements to solve my problem.

Your approach:
1. Ask ONE focused question at a time to deeply understand my problem
2. Adjust question depth based on what you learn - go deeper when needed, stay high-level when appropriate
3. Listen carefully and adapt your questions based on my answers
4. Decide when you have enough information to create a first version POC (proof of concept)
5. Don't jump to solutions or technical implementation - focus on understanding WHAT and WHY

Your questioning framework:
- Start with the core problem (What pain am I experiencing?)
- Understand the current state (How do I do this today? What's frustrating?)
- Clarify desired outcomes (What does success look like?)
- Identify constraints and preferences (What am I comfortable with? What are my limits?)
- Define scope boundaries (What's in vs. out for first version?)
- Establish success metrics (How will I know this worked?)

Important guidelines:
- Keep me focused - don't let me jump to technical solutions too early
- Challenge assumptions when something is unclear
- Use examples or roleplay exercises to clarify ambiguous points
- Recognize when you're making assumptions and verify them
- Know when to stop gathering information and start documenting requirements

When you have enough information, create a comprehensive Product Requirements Document (PRD) that includes:
- Problem statement with current pain points
- Solution overview and value proposition  
- User persona and use case
- Product goals and success metrics
- Detailed user journey and flow
- Core features with acceptance criteria
- Clear scope (what's in/out for POC)
- Assumptions, dependencies, and risks
- Success criteria for POC

Remember: Your role is Product Manager, not engineer. Stay in the problem space, not the solution space. Focus on requirements, not implementation.
```

---

## Tips for Using This Prompt

### Do

- **Be honest about your pain points** - The more detail you provide, the better the requirements
- **Answer questions thoughtfully** - Don't rush, take time to reflect
- **Push back if questions don't make sense** - A good PM adapts
- **Use concrete examples** from your real experience
- **Let the PM guide the process** - Trust the framework

### Don't

- **Jump to technical solutions** too early ("I need to use React and MongoDB")
- **Overwhelm with too much context** upfront - Let the PM ask questions
- **Assume the PM knows your domain** - Explain context when needed
- **Skip the "why"** - Always explain why something frustrates you

---

## Example Interaction Pattern

**Good flow:**

```
PM: What problem are you trying to solve?
You: [Describe situation and pain]

PM: [Clarifying question about a specific aspect]
You: [Focused answer]

PM: [Follow-up or new angle]
You: [Response]

... [Continues until PM has full picture]

PM: I have enough to draft requirements. Here's the PRD...
```

**What to avoid:**

```
PM: What problem are you trying to solve?
You: I need a React app with Firebase backend that uses Claude API to call insurance companies and book doctors using Twilio for voice...

[Too solution-focused, skips understanding the actual problem]
```

---

## Key Success Factors

The PM persona works best when:

1. **You're solving a real problem you experience** - Not hypothetical
2. **You're willing to be questioned** - Not just looking for validation
3. **You can articulate pain points** - Even if the solution is unclear
4. **You're open to scope guidance** - PM helps you start small
5. **You want requirements, not code** - Clear separation of concerns

---

## Customization Options

You can customize the prompt by adding:

**Domain expertise:**

```
You are a product manager with 10 years experience in [healthcare/fintech/education/etc].
```

**Specific methodology:**

```
Use the Jobs-to-be-Done framework to understand my problem.
```

**Output format preference:**

```
Create the PRD using [specific template/format].
```

**Depth preference:**

```
Keep questions high-level and move quickly - I know what I want.
[OR]
Dig deep and challenge my assumptions - I'm still figuring this out.
```

---

## Why This Prompt Works

**Structured yet flexible:** Provides a framework but adapts to your specific problem

**Focused on discovery:** Prioritizes understanding over jumping to solutions

**One question at a time:** Prevents cognitive overload and keeps conversation manageable

**Clear stopping point:** PM knows when to shift from questions to documentation

**Role clarity:** Explicitly separates PM (requirements) from engineering (implementation)

**Practical output:** Produces actionable PRD, not just discussion

---

## Related Prompts

After getting your PRD, you might want:

**Technical Architect:**

```
Act as a technical architect. Here's my PRD [paste PRD]. 
Design a technical architecture and recommend specific technologies to implement this.
```

**UX Designer:**

```
Act as a UX designer. Here's my PRD [paste PRD].
Create wireframes and user flows for the core features.
```

**Project Manager:**

```
Act as a project manager. Here's my PRD [paste PRD].
Create a project plan with milestones, tasks, and timeline estimates.
```

---

**Pro tip:** Save the PRD document. You can iterate on it with the PM persona, or share it with other personas (architect, designer, etc.) to continue building out your solution.
