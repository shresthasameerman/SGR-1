# Quick Reference Guide

A quick reference for common git commands and workflows for the SGR-1 project.

## Quick Start

```bash
# Clone the repository
git clone https://github.com/shresthasameerman/SGR-1.git
cd SGR-1

# Create a new prototype branch
git checkout -b prototype/my-feature

# Make changes, then commit
git add .
git commit -m "feat: add my feature"

# Push to remote
git push -u origin prototype/my-feature
```

## Common Commands

### Creating a Branch

```bash
# Create and switch to a new prototype branch
git checkout -b prototype/<feature-name>

# Push to remote
git push -u origin prototype/<feature-name>
```

### Updating Your Branch

```bash
# Get latest changes from main
git checkout main
git pull origin main

# Switch back and merge
git checkout prototype/<feature-name>
git merge main

# Push updates
git push
```

### Checking Status

```bash
# See current branch and uncommitted changes
git status

# See commit history
git log --oneline -10

# See branches
git branch -a
```

### Making Changes

```bash
# Stage all changes
git add .

# Stage specific files
git add file1.txt file2.txt

# Commit with message
git commit -m "your message"

# Push to remote
git push
```

### Viewing Changes

```bash
# See unstaged changes
git diff

# See staged changes
git diff --cached

# See changes between branches
git diff main..prototype/<feature-name>

# See commit history
git log --oneline --graph
```

### Handling Conflicts

```bash
# When conflicts occur during merge
# 1. Edit files to resolve conflicts
# 2. Remove conflict markers (<<<<, ====, >>>>)
# 3. Stage resolved files
git add <resolved-files>

# 4. Complete the merge
git commit -m "Resolve merge conflicts"

# 5. Push
git push
```

### Undoing Changes

```bash
# Discard uncommitted changes to a file
git checkout -- <file>

# Unstage a file
git reset HEAD <file>

# Undo last commit (keeps changes)
git reset --soft HEAD~1

# Undo last commit (discards changes) - USE WITH CAUTION
git reset --hard HEAD~1
```

### Branch Management

```bash
# List all branches
git branch -a

# Delete local branch
git branch -d prototype/<feature-name>

# Delete remote branch
git push origin --delete prototype/<feature-name>

# Rename current branch
git branch -m new-branch-name
```

## Workflow Cheat Sheet

### Daily Workflow

```bash
# 1. Start your day - update main
git checkout main
git pull origin main

# 2. Switch to your prototype branch
git checkout prototype/<your-feature>

# 3. Merge latest main
git merge main

# 4. Work on your feature
# ... make changes ...

# 5. Commit your work
git add .
git commit -m "descriptive message"

# 6. Push to remote
git push
```

### Pre-Merge Workflow

```bash
# 1. Ensure you're on your branch
git checkout prototype/<your-feature>

# 2. Update with main
git checkout main
git pull origin main
git checkout prototype/<your-feature>
git merge main

# 3. Resolve any conflicts
# ... fix conflicts ...
git add .
git commit -m "Resolve conflicts"

# 4. Test your changes
# ... run tests ...

# 5. Push final version
git push

# 6. Create PR on GitHub
```

## Branch Naming Examples

```bash
# Good names
prototype/user-authentication
prototype/payment-gateway
prototype/dark-mode
prototype/api-refactor
prototype/mobile-responsive

# Bad names
mywork
test
feature
new-stuff
```

## Commit Message Examples

```bash
# Feature additions
git commit -m "feat: add user login form"
git commit -m "feat: implement payment processing"

# Bug fixes
git commit -m "fix: resolve navbar overlap on mobile"
git commit -m "fix: correct date formatting in reports"

# Documentation
git commit -m "docs: update README with installation steps"
git commit -m "docs: add API documentation"

# Refactoring
git commit -m "refactor: simplify user authentication logic"
git commit -m "refactor: extract common utilities"

# Style changes
git commit -m "style: format code with prettier"
git commit -m "style: update button colors"

# Tests
git commit -m "test: add unit tests for auth module"
git commit -m "test: increase coverage for API endpoints"
```

## Troubleshooting

### "Nothing to commit, working tree clean"

Your changes are already committed. Use `git status` to confirm.

### "Your branch is ahead of 'origin/...' by N commits"

You have local commits not pushed to remote. Use `git push`.

### "Your branch is behind 'origin/...' by N commits"

Remote has changes you don't have locally. Use `git pull`.

### "Updates were rejected because the remote contains work..."

Remote has different commits. Pull first, resolve conflicts, then push:
```bash
git pull origin prototype/<your-feature>
# resolve any conflicts
git push
```

### "Merge conflict in <file>"

Edit the file, remove conflict markers, then:
```bash
git add <file>
git commit -m "Resolve merge conflict"
```

### "fatal: not a git repository"

You're not in the repository directory. Navigate to it:
```bash
cd /path/to/SGR-1
```

## Useful Aliases

Add these to your `~/.gitconfig`:

```ini
[alias]
    st = status
    co = checkout
    br = branch
    cm = commit -m
    lg = log --oneline --graph --all
    last = log -1 HEAD
    unstage = reset HEAD --
    discard = checkout --
```

Usage:
```bash
git st        # instead of git status
git co main   # instead of git checkout main
git br        # instead of git branch
git cm "msg"  # instead of git commit -m "msg"
git lg        # pretty log
```

## Resources

- [BRANCHING_GUIDE.md](BRANCHING_GUIDE.md) - Detailed branching strategy
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contributing guidelines
- [MERGE_WORKFLOW.md](MERGE_WORKFLOW.md) - Merge process details
- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
- [Git Documentation](https://git-scm.com/doc)

## Getting Help

- Use `git help <command>` for command details
- Check project documentation
- Ask team members
- Search GitHub issues
