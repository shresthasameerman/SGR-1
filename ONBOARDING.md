# Team Onboarding Guide

Welcome to the SGR-1 project! This guide will help you get started with our collaborative prototyping workflow.

## What is SGR-1?

SGR-1 is a collaborative prototyping repository where team members can work on different features in parallel using separate branches, which can later be merged into the main branch.

## Prerequisites

Before you start, ensure you have:

- [ ] Git installed on your computer ([Download Git](https://git-scm.com/downloads))
- [ ] A GitHub account ([Sign up](https://github.com/join))
- [ ] Access to the SGR-1 repository (ask the repository owner for access)
- [ ] Basic understanding of Git commands (see resources below)

## First-Time Setup

### Step 1: Clone the Repository

Open your terminal/command prompt and run:

```bash
git clone https://github.com/shresthasameerman/SGR-1.git
cd SGR-1
```

### Step 2: Configure Git (if not already done)

Set your name and email:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Step 3: Verify Your Setup

Check that everything is working:

```bash
git status
git branch -a
```

You should see the current branch and repository status.

## Your First Prototype

Let's create your first prototype branch!

### Step 1: Plan Your Prototype

Decide what feature or experiment you want to work on. Examples:
- User authentication system
- Data visualization dashboard
- API integration
- UI component

### Step 2: Create Your Branch

```bash
# Make sure you're on the main branch and it's up to date
git checkout main
git pull origin main

# Create your prototype branch
git checkout -b prototype/your-feature-name
```

Replace `your-feature-name` with a descriptive name (e.g., `user-login`, `dark-theme`, `api-client`).

### Step 3: Make Your First Changes

1. Create or modify files as needed
2. Check what changed:
   ```bash
   git status
   ```

3. Stage your changes:
   ```bash
   git add .
   ```

4. Commit your changes:
   ```bash
   git commit -m "feat: initial implementation of <feature>"
   ```

### Step 4: Push to GitHub

```bash
git push -u origin prototype/your-feature-name
```

The `-u` flag sets up tracking, so future pushes only need `git push`.

### Step 5: Continue Working

As you work:

```bash
# Make changes to files
# Stage changes
git add .

# Commit with a descriptive message
git commit -m "feat: add user registration form"

# Push to keep remote updated
git push
```

## Daily Workflow

### Morning Routine

```bash
# Switch to main and update
git checkout main
git pull origin main

# Switch to your prototype branch
git checkout prototype/your-feature-name

# Merge latest changes from main
git merge main

# If there are conflicts, resolve them
# Then continue working
```

### During the Day

```bash
# Check status frequently
git status

# Commit often
git add .
git commit -m "your message"
git push
```

### End of Day

```bash
# Make sure all work is committed and pushed
git status
git push
```

## When Your Prototype is Ready

### Step 1: Prepare for Merge

```bash
# Update with latest main
git checkout main
git pull origin main
git checkout prototype/your-feature-name
git merge main

# Resolve conflicts if any
# Test everything works
# Push final version
git push
```

### Step 2: Create a Pull Request

1. Go to GitHub: https://github.com/shresthasameerman/SGR-1
2. Click "Pull requests" tab
3. Click "New pull request"
4. Select:
   - Base: `main`
   - Compare: `prototype/your-feature-name`
5. Fill out the PR template
6. Click "Create pull request"

### Step 3: Wait for Review

- Team members will review your code
- Address any feedback by making changes locally and pushing
- Once approved, your PR can be merged

### Step 4: After Merge

```bash
# Switch to main and update
git checkout main
git pull origin main

# Optional: Delete your local branch
git branch -d prototype/your-feature-name

# Optional: Delete remote branch
git push origin --delete prototype/your-feature-name

# Start a new prototype!
git checkout -b prototype/next-feature
```

## Common Scenarios

### Scenario 1: I Made a Mistake in My Last Commit

```bash
# Undo last commit but keep changes
git reset --soft HEAD~1

# Make corrections
git add .
git commit -m "corrected message"
```

### Scenario 2: I Want to Start Over on a File

```bash
# Discard all changes to a specific file
git checkout -- filename.txt
```

### Scenario 3: My Branch is Behind Main

```bash
# Update your branch with main
git checkout main
git pull origin main
git checkout prototype/your-feature
git merge main
git push
```

### Scenario 4: I Have Merge Conflicts

When you see conflict markers in files:

1. Open the conflicted file
2. Look for:
   ```
   <<<<<<< HEAD
   your changes
   =======
   changes from main
   >>>>>>> main
   ```
3. Edit the file to keep the correct code
4. Remove the conflict markers
5. Save the file
6. Stage and commit:
   ```bash
   git add filename.txt
   git commit -m "Resolve merge conflict"
   git push
   ```

### Scenario 5: I Need to Switch Branches But Have Uncommitted Changes

Option 1 - Commit your work:
```bash
git add .
git commit -m "WIP: work in progress"
git checkout other-branch
```

Option 2 - Stash your work:
```bash
git stash
git checkout other-branch
# Later, return and restore:
git checkout original-branch
git stash pop
```

## Best Practices for New Team Members

1. **Commit Often**: Small, frequent commits are better than large ones
2. **Write Clear Messages**: Use descriptive commit messages
3. **Stay Updated**: Merge main into your branch regularly (at least daily)
4. **Ask Questions**: If unsure, ask team members
5. **Test Your Work**: Make sure your prototype works before creating a PR
6. **Read Documentation**: Familiarize yourself with all project docs

## Quick Command Reference

```bash
# See current status
git status

# See commit history
git log --oneline -10

# See all branches
git branch -a

# Switch branches
git checkout branch-name

# Create and switch to new branch
git checkout -b new-branch-name

# Stage all changes
git add .

# Commit
git commit -m "message"

# Push
git push

# Pull latest changes
git pull

# See what changed
git diff
```

## Documentation Resources

Read these documents to learn more:

1. **[README.md](README.md)**: Project overview and quick start
2. **[BRANCHING_GUIDE.md](BRANCHING_GUIDE.md)**: Detailed branching workflow
3. **[CONTRIBUTING.md](CONTRIBUTING.md)**: Contribution guidelines
4. **[MERGE_WORKFLOW.md](MERGE_WORKFLOW.md)**: How to merge prototypes
5. **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)**: Command cheat sheet

## Learning Git

New to Git? Check out these resources:

- [Git Official Documentation](https://git-scm.com/doc)
- [GitHub Git Guides](https://github.com/git-guides)
- [Interactive Git Tutorial](https://learngitbranching.js.org/)
- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)

## Getting Help

If you need help:

1. Check the documentation in this repository
2. Search for your issue on [Stack Overflow](https://stackoverflow.com/questions/tagged/git)
3. Ask team members in your project chat
4. Refer to Git's built-in help: `git help <command>`

## Troubleshooting

### "Permission denied" error

You may not have access to the repository. Contact the repository owner.

### "fatal: not a git repository"

You're not in the repository directory. Navigate to it:
```bash
cd /path/to/SGR-1
```

### "Updates were rejected"

Someone else pushed changes. Pull first, then push:
```bash
git pull
git push
```

### Lost or confused?

You can always check where you are:
```bash
pwd           # Current directory
git status    # Git status
git branch    # Current branch
```

## Next Steps

Now that you're set up:

1. Read through the [BRANCHING_GUIDE.md](BRANCHING_GUIDE.md)
2. Create your first prototype branch
3. Make some changes and commit them
4. Push to GitHub and see your branch there
5. When ready, create your first Pull Request

Welcome to the team! Happy coding! 🚀
