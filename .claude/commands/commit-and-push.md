# /commit-and-push - Commit and Push Learning Notes

Invoke the release-manager agent to commit all completed work and push to the remote GitHub repository.

## When to Use

Use this command when you want to:

- Save your learning notes to GitHub
- Commit lecture notes updates
- Push documentation changes
- Store code examples or experiments

## What It Does

The release-manager agent will:

1. Review all changes (`git status`, `git diff`)
2. Create a meaningful commit message following conventional commit format
3. Commit the changes locally
4. Push to GitHub remote repository
5. Report what was committed

Use the Task tool to invoke the release-manager agent to commit all changes and push to the remote GitHub repository.