# Writing Claude.md Files

## What is Claude.md?

Claude.md is your AI team member's persistent memory - essential context that's available in every prompt. Just like onboarding a new developer, you need to provide Claude Code with the institutional knowledge it needs to work effectively on your team.

### The CONTEXT Framework for Claude.md Design

Use this acronym to remember the key principles:

- Clear and Concise Instructions
- Operational Processes
- Naming and Standards
- Testing and Quality Gates
- Examples and References
- Expectations and Boundaries

Tools and Dependencies

### Core Principles

**1. Essential Information Only**

Claude.md should contain global information that applies to every task. Don't overwhelm it with project-specific details that only apply to certain features.

**2. Specificity Creates Better Targets**

Context narrows the target from broad instructions to precise outcomes. "Write solid code" is vague; "Follow SOLID design principles for all object-oriented code" is actionable.

**3. Process Over Micromanagement**

Define workflows and checks, not implementation details. Let Claude make architectural decisions within your guardrails.

## Examples

- [Open Source Library Development](./claude.md.examples/open-source-library-development.md)
- [DevOps Infrastructure Project](./claude.md.examples/devops-infrastructure-project.md)
- [Enterprise Backend Service](./claude.md.examples/enterprize-backend-service.md)
- [Mobile App Development (React Native)](./claude.md.examples/mobile-app-development-react-native.md)
- [Python Data Science Project](./claude.md.examples/python-data-science-project.md)
- [Web Application Development Team](./claude.md.examples/web-application-development-team.md)

**Best Practice Summaries**:

- DO's

  - ✅ Use clear, actionable language
  - ✅ Provide specific tools and frameworks
  - ✅ Define quality gates and testing requirements
  - ✅ Include workflow processes
  - ✅ Specify naming conventions
  - ✅ Reference established design principles
- DON'ts:
  - ❌ Include task-specific details that only apply sometimes
  - ❌ Write 1000-page documentation dumps
  - ❌ Use vague instructions like "write good code"
  - ❌ Forget to specify version control workflows
  - ❌ Micromanage implementation details
  - ❌ Include temporary or changing information
