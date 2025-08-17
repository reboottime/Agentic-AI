# Module 2: AI Agent Design Principles & Safety

## Progress

- [x] The MATE Design Principles for AI Agents
- [x] MATE Design Principles in Code
- [ ] AI Agents & Environment Safety

## Question List

## Notes

- [x] discussing principles from software engineer practice perspective
  - M: [how to choose right model](./01.the-mate-design-principle.md#m---model-efficiency)
  - A: [how to design action and why](./01.the-mate-design-principle.md#a---action-specificity)
  - T: [why and how to improve token efficiency](./01.the-mate-design-principle.md#t---token-efficiency)
  - E: [**Design safe environments where actions are secure and reversible.**](./01.the-mate-design-principle.md#e---environment-safety)
- [x] [MATE Design Principles in Code](./02.MATE%20Design%20Principles%20in%20Code.md)
- [x] [Environmental Safety for AI Agents](./03.ai-agent-and-environment-safety.md)
  - reversible action: The key to making actions reversible is capturing enough information during execution to fully reverse the operation later. See [code here](./03.ai-agent-and-environment-safety.md#pattern-1-reversible-actions).
  - transaction management: Transaction management allows us to treat a group of related actions as a single unit that either fully succeeds or fully fails. This pattern is especially effective when combined with reversible actions. If any step in a multi-step process fails, all previous steps can be automatically rolled back. See [code here](./03.ai-agent-and-environment-safety.md#pattern-2-transaction-management).
  - Staged Execution with Review: Staged execution lets us plan a series of actions, review them for safety and correctness, and only then execute them. See [code pattern here](./03.ai-agent-and-environment-safety.md#pattern-3-staged-execution-with-review).
    - [ ] I do not get it. The sample code intentionally makes flaws to demonstrate the small context problem. So the theory makes senses to me from intuition, but I need real experience to get buy in.

## Insights

[The principles in playing chess](https://www.coursera.org/learn/ai-agents-architecture-python/ungradedWidget/65nG7/mate-design-principles-in-code). Gus in Breaking Bad applies these principles really well.

> In chess, a checkmate represents the perfect execution of strategy - every piece positioned correctly, every move calculated for maximum effect, leading to an inevitable victory. When building AI agents, we can apply similar strategic thinking through the MATE principles: Model efficiency, Action specificity, Token efficiency, and Environmental safety.
