# Allowing Claude Code to Work in Parallel with Git Worktrees

## Git Worktrees with Claude Code: Parallel Development in Isolation

`Git worktrees combined with Claude Code create a powerful workflow for parallel development.` `Instead of juggling multiple branches on a single working directory, you can have multiple isolated environments where different Claude Code instances work simultaneously on separate features without any conflicts.`

### What Are Git Worktrees?

`Git worktrees allow you to check out multiple branches from the same repository into separate directories.` `Each worktree has its own working directory with isolated files, while sharing the same Git history and reflog.`

Think of it this way:

- **Traditional workflow:** One working directory, switch between branches
- **Worktree workflow:** Multiple working directories, each with its own branch

### Setting Up Parallel Development Environments

#### Creating Your First Worktree

Let's say you're working on your expense tracker app and need to develop two features simultaneously: a data export system and an analytics dashboard.

### Step 1: Ask Claude Code to Set Up Worktrees

```md
I want to develop two features in parallel for my expense tracker app using Git worktrees:

1. Data export system (CSV, PDF, JSON exports)
2. Analytics dashboard (charts, insights, trends)

Please help me set up the worktree environment:
1. Create a worktree for the export feature at ../expense-tracker-export with branch 
feature/data-export
2. Create a worktree for the analytics feature at ../expense-tracker-analytics with branch 
feature/analytics-dashboard
3. List all worktrees to confirm they were created
4. Explain what each worktree will contain and how they're isolated

I want to be able to work on both features simultaneously without conflicts.
```

Your directory structure now looks something like:

`/expense-tracker-ai/         # Main worktree (main branch)`

`/expense-tracker-export/     # Export worktree (feature/data-export)`

`/expense-tracker-analytics/  # Analytics worktree (feature/analytics-dashboard)`


**Launching Claude Code in Each Worktree**:

Each worktree is a complete, independent development environment. Now, open two different terminal windows and start Claude Code in each of the separate worktrees:

- **Terminal 1- Export Feature**:
```md
cd ../expense-tracker-export
claude
```

- **Terminal 2 - Analytics Feature:**

```md
cd ../expense-tracker-analytics
claude

```

**You can now safely run Claude Code in parallel to develop multiple expense tracker features simultaneously.**Each worktree operates in complete isolation - changes made in one worktree won't affect the others, and you can test each feature independently without any conflicts. This means you can have Claude working on your export system in one terminal while simultaneously developing the analytics dashboard in another, all without the risk of breaking existing functionality or interfering with each other's work. The parallel development approach allows you to make rapid progress on multiple fronts while maintaining clean, conflict-free code.

### Merging Worktree Features Back to Main

#### Prerequisites

- You have completed features in separate worktrees
- Features are committed and working in their respective branches
- You're in the main project directory on the original branch you built worktrees off of
- Stop Claude Code in each of the separate terminals so that you don't confuse yourself!
- Run Claude Code in the main project directory on the original branch


### Step 1: Ask Claude Code to Handle the Integration

```md
I have two features developed in parallel worktrees that I need to integrate:
- feature/data-export (export functionality)
- feature/analytics-dashboard (analytics functionality)

Please help me integrate these features:
1. Create a new integration branch called "integration/export-analytics"
2. Merge feature/data-export into the integration branch
3. Merge feature/analytics-dashboard into the integration branch
4. Resolve any merge conflicts that arise
5. Test that both features work together
6. Run all tests to ensure nothing is broken

I want to integrate these safely before merging to main.
```


#### Result

Your parallel features are now integrated into your main branch, and all worktrees are cleaned up. Test your application to ensure everything works together!


#### Make These Reusable Commands!

Parallel Work Command

Save this as `.claude/commands/parallel-work.md`


```md
I want to develop features in parallel for my expense tracker app using Git worktrees: $ARGUMENTS

Think about how to divide the work up into separate features unless this has been 
clearly explained already. 

Please help me set up the worktree environment:
1. For each feature mentioned, create a worktree at ../expense-tracker-[feature-name] 
with branch feature/[feature-name]
2. Set up the development environment in each worktree
3. List all worktrees to confirm they were created
4. Explain what each worktree will contain and how they're isolated

I want to be able to work on all features simultaneously without conflicts.
```

### Integration Command

#### Integrate Parallel Work Command

Save this as `.claude/commands/integrate-parallel-work.md`

```md
I have features developed in parallel worktrees that I need to integrate: $ARGUMENTS

Please help me integrate these features:
1. Create a new integration branch called "integration/parallel-features"
2. For each feature name provided, merge the branch feature/[feature-name] into the integration branch
3. Resolve any merge conflicts that arise
4. Test that all features work together
5. Run all tests to ensure nothing is broken
6. Once integration is successful, merge to main and clean up branches

I want to integrate these safely before merging to main.
```

Example Command Usage:

`/integrate-parallel-work budget-tracking notifications user-settings`

