# Merge Workflow Guide

This guide provides detailed instructions for merging prototype branches into the main branch.

## Pre-Merge Checklist

Before creating a Pull Request to merge your prototype:

- [ ] All code is committed and pushed
- [ ] Code follows project standards
- [ ] All tests pass (if applicable)
- [ ] Documentation is updated
- [ ] Branch is up to date with main
- [ ] Conflicts are resolved
- [ ] Code has been reviewed (self-review at minimum)

## Step-by-Step Merge Process

### 1. Prepare Your Branch

Ensure your prototype branch is ready for merge:

```bash
# Switch to your prototype branch
git checkout prototype/<your-feature-name>

# Check status
git status

# Commit any pending changes
git add .
git commit -m "Final changes before merge"
```

### 2. Update with Main Branch

Always update your branch with the latest main before merging:

```bash
# Fetch latest changes
git fetch origin

# Switch to main and update
git checkout main
git pull origin main

# Switch back to your branch
git checkout prototype/<your-feature-name>

# Merge main into your branch
git merge main
```

### 3. Resolve Conflicts (if any)

If conflicts occur during the merge:

```bash
# Git will list conflicted files
# Open each file and look for conflict markers:
# <<<<<<< HEAD
# your changes
# =======
# changes from main
# >>>>>>> main

# Edit files to resolve conflicts
# Remove conflict markers
# Keep the code that should remain

# After resolving, stage the files
git add <resolved-files>

# Complete the merge
git commit -m "Resolve merge conflicts with main"
```

### 4. Test After Merging

After merging main into your branch:

```bash
# Run tests if available
# npm test
# python -m pytest
# ./run_tests.sh

# Verify functionality manually
# Check that nothing broke
```

### 5. Push Updated Branch

```bash
git push origin prototype/<your-feature-name>
```

### 6. Create Pull Request

On GitHub:

1. Navigate to the repository
2. Click "Pull requests" tab
3. Click "New pull request"
4. Select:
   - Base: `main`
   - Compare: `prototype/<your-feature-name>`
5. Fill in the PR template:

   **Title**: Clear, descriptive title (e.g., "Add user authentication prototype")
   
   **Description**:
   ```
   ## Summary
   Brief description of what this prototype does
   
   ## Changes
   - List of key changes
   - Features added
   - Files modified
   
   ## Testing
   How to test this prototype
   
   ## Screenshots (if UI changes)
   Include relevant screenshots
   
   ## Notes
   Any additional context, limitations, or future work
   ```

6. Assign reviewers (if applicable)
7. Add labels (if applicable)
8. Click "Create pull request"

### 7. Code Review Process

Once the PR is created:

1. **Wait for reviews**: Team members will review your code
2. **Address feedback**: 
   - Make requested changes in your local branch
   - Commit and push the changes
   - Comment on the PR to notify reviewers
3. **Respond to comments**: 
   - Answer questions
   - Explain your approach if needed
   - Be open to suggestions

### 8. Merge the PR

After approval:

1. **Final check**: Ensure all CI checks pass (if configured)
2. **Choose merge method**:
   - **Create a merge commit**: Preserves full history (recommended for prototypes)
   - **Squash and merge**: Combines all commits into one
   - **Rebase and merge**: Reapplies commits on top of main
3. Click the merge button
4. Confirm the merge

### 9. Clean Up

After successful merge:

```bash
# Switch to main and update
git checkout main
git pull origin main

# Delete local prototype branch (optional)
git branch -d prototype/<your-feature-name>

# Delete remote prototype branch (optional)
git push origin --delete prototype/<your-feature-name>
```

## Handling Complex Merges

### Large Conflicts

If you have many conflicts:

1. Consider breaking your prototype into smaller parts
2. Merge main into your branch more frequently
3. Coordinate with team members working on related areas
4. Use a merge tool:
   ```bash
   git mergetool
   ```

### Long-Running Branches

For prototypes that take days or weeks:

1. Merge main into your branch daily or weekly
2. Keep your branch updated to minimize conflicts
3. Communicate with the team about your work
4. Consider breaking into smaller PRs

### Failed Merges

If a merge causes issues:

1. The main branch should remain stable
2. If problems are discovered after merge:
   - Create a hotfix branch
   - Fix the issue
   - Create a new PR
3. If the merge must be reverted:
   ```bash
   # On main branch
   git revert -m 1 <merge-commit-hash>
   git push origin main
   ```

## Merge Strategies

### Feature Complete

When a prototype is fully complete:
- Merge the entire branch
- All commits become part of main history
- Good for significant features

### Incremental Merge

For large prototypes:
- Create multiple smaller PRs
- Each PR contains a working subset
- Easier to review and test
- Reduces risk

### Squash Merge

For messy commit history:
- Combines all commits into one
- Cleaner main branch history
- Loses individual commit details
- Good for experimental work with many "WIP" commits

## Communication During Merge

### Before Merge

- Announce significant merges to the team
- Check if anyone is working on related code
- Coordinate timing to avoid conflicts

### During Review

- Respond promptly to review comments
- Be receptive to feedback
- Explain your decisions clearly

### After Merge

- Announce successful merge
- Document any known issues
- Update team on next steps

## Merge Conflicts - Common Scenarios

### Scenario 1: Same File, Different Lines

Usually easy to resolve - Git can often handle automatically.

### Scenario 2: Same File, Same Lines

Requires manual resolution:
- Review both changes
- Decide which to keep or combine
- Test thoroughly after resolution

### Scenario 3: File Renamed or Moved

May require manual intervention:
- Check if both sides renamed the file
- Ensure references are updated
- Verify imports/includes

### Scenario 4: Dependency Conflicts

Package.json, requirements.txt, etc.:
- Keep both dependencies if needed
- Update versions to compatible ones
- Test with both dependencies

## Best Practices

1. **Merge main into your branch frequently** - Don't let your branch get too far behind
2. **Keep PRs focused** - Easier to review and less likely to conflict
3. **Test before merging** - Catch issues early
4. **Document thoroughly** - Help reviewers understand your changes
5. **Communicate** - Let the team know about significant changes
6. **Don't merge broken code** - Main should always be stable

## Tools and Tips

### Viewing Differences

```bash
# See what changed in your branch
git diff main...prototype/<your-feature-name>

# See commits that will be merged
git log main..prototype/<your-feature-name>
```

### Checking Status

```bash
# See if your branch is behind main
git fetch origin
git status

# See divergence
git rev-list --left-right --count main...prototype/<your-feature-name>
```

### Conflict Resolution Tools

- Git built-in merge tool: `git mergetool`
- VS Code: Built-in merge conflict resolver
- GitHub Desktop: Visual merge conflict resolution
- Beyond Compare, KDiff3, Meld: Third-party tools

## Rollback Plan

If a merge causes issues:

### Option 1: Revert the Merge

```bash
git revert -m 1 <merge-commit-hash>
git push origin main
```

### Option 2: Fix Forward

```bash
git checkout -b hotfix/fix-merge-issue
# Make fixes
git commit -m "Fix issues from prototype merge"
# Create new PR
```

## Summary

Remember:
- Update your branch with main before merging
- Resolve conflicts carefully
- Test thoroughly
- Get code reviewed
- Keep main stable
- Communicate with the team

For more details, see [BRANCHING_GUIDE.md](BRANCHING_GUIDE.md) and [CONTRIBUTING.md](CONTRIBUTING.md).
