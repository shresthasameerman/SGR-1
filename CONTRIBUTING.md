# Contributing to SGR-1

Thank you for contributing to SGR-1! This document provides guidelines for contributing to the project.

## Getting Started

1. Fork the repository (if you're an external contributor)
2. Clone your fork or the main repository:
   ```bash
   git clone https://github.com/shresthasameerman/SGR-1.git
   cd SGR-1
   ```

3. Create a prototype branch for your work:
   ```bash
   git checkout -b prototype/<your-feature-name>
   ```

## Branch Naming Conventions

We use a structured branch naming convention to keep the repository organized:

### Prototype Branches

Format: `prototype/<descriptive-name>`

**Examples:**
- `prototype/user-authentication`
- `prototype/payment-integration`
- `prototype/mobile-responsive`
- `prototype/dark-mode`

### Guidelines:
- Use lowercase letters only
- Separate words with hyphens (kebab-case)
- Be descriptive but concise
- Always use the `prototype/` prefix for experimental features

## Commit Messages

Write clear and meaningful commit messages:

### Format:
```
<type>: <subject>

<body (optional)>
```

### Types:
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### Examples:
```
feat: add user login functionality

Implemented basic user authentication with email and password.
Includes form validation and error handling.
```

```
fix: resolve navbar display issue on mobile

The navigation bar was not responsive on mobile devices.
Updated CSS to use flexbox layout.
```

## Pull Request Process

1. **Update your branch** with the latest main:
   ```bash
   git checkout main
   git pull origin main
   git checkout prototype/<your-feature-name>
   git merge main
   ```

2. **Push your changes**:
   ```bash
   git push -u origin prototype/<your-feature-name>
   ```

3. **Create a Pull Request** on GitHub:
   - Provide a clear title
   - Describe what your prototype does
   - List any dependencies or requirements
   - Mention any known issues or limitations
   - Reference any related issues

4. **Respond to feedback**:
   - Address review comments
   - Make requested changes
   - Push updates to your branch

5. **Merge when approved**:
   - Wait for approval from maintainers
   - Ensure all checks pass
   - Merge using the project's preferred method

## Code Standards

- Write clean, readable code
- Comment complex logic
- Follow existing code style in the project
- Keep functions and modules focused
- Remove debug code and commented-out code before committing

## Testing

- Test your prototype thoroughly before submitting a PR
- Include any test files or instructions
- Document how to test your changes

## Documentation

- Update README.md if you add new features
- Add inline comments for complex code
- Include usage examples if applicable
- Document any new dependencies

## Communication

- Be respectful and constructive
- Ask questions if you're unsure
- Provide helpful feedback on others' PRs
- Keep discussions focused and professional

## Project Structure

Currently, the project structure is minimal:
```
SGR-1/
├── LICENSE
├── README.md
├── BRANCHING_GUIDE.md
└── CONTRIBUTING.md
```

As prototypes are developed, the structure will evolve. Document any significant structural changes in your PRs.

## Questions?

If you have questions about contributing:
- Check the BRANCHING_GUIDE.md for workflow details
- Open an issue for discussion
- Reach out to project maintainers

Thank you for contributing to SGR-1!
