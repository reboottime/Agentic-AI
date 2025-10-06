# Claude Subagents & Tasks

Subagents are one of Claude Code's most powerful features for handling complex projects and large codebases. They allow you to run multiple specialized Claude instances in parallel, each with their own context and focus area.

## What Are Subagents?

Subagents are lightweight instances of Claude Code running in a task via the Task Tool. When a subagent is running, you can actually see that the output says "Task(Performing task X)".

The key benefits of subagents include:

* **Independent context windows:** Each subagent maintains its own context, preventing information overflow
* **Parallel execution:** Multiple subagents can work simultaneously on different aspects of your project
* **Specialized focus:** Each subagent can be given a specific domain or task to concentrate on

## Basic Subagent Usage

### Running Two Specialized Subagents

Here's a practical example of running two subagents to analyze different parts of your application:

```md
1 Can you run two subagents?
2 One of them should analyze improvements to the back-end that could be made.
3 One of them should analyze improvements that could be made to the front end.
4 Please run them in parallel.
```

When you run this command, Claude Code will create two parallel tasks:
Each subagent will:

* Focus exclusively on their assigned domain (backend vs frontend)
* Use their own context window to dive deep into relevant files
* Provide specialized recommendations based on their area of expertise

### Exploring Large Codebases

One interesting fact is that you can actually run multiple subagents in parallel. For example, you can launch 4 parallel tasks with this prompt:

```md
1 Explore the codebase using 4 tasks in parallel.
2 Each agent should explore different directories.
```

This approach is particularly valuable for:

* **Large codebases:** When you need to understand multiple components quickly
* **Initial project assessment:** Getting a comprehensive overview without overwhelming a single context window
* **Domain separation:** Having different subagents focus on different architectural layers
