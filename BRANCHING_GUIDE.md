# Branching Guide for SGR-1

This guide outlines the branching strategy for the SGR-1 project to enable efficient team collaboration on prototypes.

## Branch Structure

### Main Branches

- **main** (or **master**): The primary branch containing production-ready code
  - All prototype branches should eventually merge here
  - Protected branch with review requirements
  - Always in a deployable state

### Prototype Branches

Prototype branches are used for experimental features and proof-of-concepts. They follow the naming convention:

```
prototype/<feature-name>
```

**Examples:**
- `prototype/user-authentication`
- `prototype/data-visualization`
- `prototype/api-integration`
- `prototype/ui-redesign`

## Workflow

### Creating a Prototype Branch

1. Ensure your local main branch is up to date:
   ```bash
   git checkout main
   git pull origin main
   ```

2. Create a new prototype branch:
   ```bash
   git checkout -b prototype/<your-feature-name>
   ```

3. Push the branch to remote:
   ```bash
   git push -u origin prototype/<your-feature-name>
   ```

### Working on a Prototype

1. Make your changes and commit regularly:
   ```bash
   git add .
   git commit -m "Description of changes"
   ```

2. Push changes to keep remote updated:
   ```bash
   git push
   ```

3. Keep your branch updated with main:
   ```bash
   git checkout main
   git pull origin main
   git checkout prototype/<your-feature-name>
   git merge main
   ```

### Merging a Prototype into Main

When your prototype is ready for integration:

1. Ensure all tests pass and code is reviewed
2. Update your branch with the latest main:
   ```bash
   git checkout main
   git pull origin main
   git checkout prototype/<your-feature-name>
   git merge main
   ```

3. Resolve any conflicts if they exist

4. Create a Pull Request (PR) on GitHub:
   - Go to the repository on GitHub
   - Click "New Pull Request"
   - Select your prototype branch as the source
   - Select main as the target
   - Fill in the PR description with:
     - What the prototype does
     - Any testing done
     - Known issues or limitations

5. Wait for review and approval

6. Merge the PR when approved

7. Delete the prototype branch after merging (optional):
   ```bash
   git branch -d prototype/<your-feature-name>
   git push origin --delete prototype/<your-feature-name>
   ```

## Best Practices

1. **Keep branches focused**: Each prototype branch should focus on a single feature or experiment
2. **Commit often**: Make small, logical commits with clear messages
3. **Stay updated**: Regularly merge main into your prototype branch to avoid large conflicts
4. **Document your work**: Add README files or comments explaining your prototype
5. **Test thoroughly**: Ensure your prototype works before requesting a merge
6. **Clean up**: Delete branches after they're merged to keep the repository organized

## Branch Naming Conventions

- Use lowercase letters
- Use hyphens to separate words
- Be descriptive but concise
- Always prefix with `prototype/`

**Good examples:**
- `prototype/user-auth`
- `prototype/dashboard-redesign`
- `prototype/api-v2`

**Bad examples:**
- `prototype/mywork` (not descriptive)
- `prototype/USER_AUTH` (uses uppercase)
- `my-feature` (missing prototype prefix)

## Handling Conflicts

When merging main into your prototype branch, conflicts may occur:

1. Git will mark conflicted files
2. Open each file and resolve conflicts manually
3. Remove conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
4. Test the resolved code
5. Commit the resolution:
   ```bash
   git add .
   git commit -m "Resolve merge conflicts with main"
   git push
   ```

## Getting Help

If you encounter issues:
- Check this guide and CONTRIBUTING.md
- Ask team members for assistance
- Review GitHub's documentation on branching and merging
