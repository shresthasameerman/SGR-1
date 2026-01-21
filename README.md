# SGR-1

A collaborative prototyping repository where team members can work on different features in parallel and merge them into the main branch.

## Overview

This repository is designed to support team collaboration through a structured branching workflow. Each team member can create prototype branches to experiment with features, which can later be merged into the main branch once they're ready.

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/shresthasameerman/SGR-1.git
cd SGR-1
```

### Create a Prototype Branch

```bash
git checkout -b prototype/<your-feature-name>
```

### Make Changes and Commit

```bash
git add .
git commit -m "Your commit message"
git push -u origin prototype/<your-feature-name>
```

### Merge into Main

When your prototype is ready, create a Pull Request to merge it into the main branch.

## Documentation

- **[Branching Guide](BRANCHING_GUIDE.md)**: Detailed branching strategy and workflow
- **[Contributing Guidelines](CONTRIBUTING.md)**: How to contribute to the project

## Branch Structure

- **main**: The primary branch containing stable, production-ready code
- **prototype/\***: Feature prototype branches for experimental work

## Workflow Summary

1. Create a prototype branch from main
2. Develop your feature on your branch
3. Keep your branch updated by regularly merging main
4. Create a Pull Request when ready
5. Get your changes reviewed
6. Merge into main after approval

## Best Practices

- Keep prototype branches focused on a single feature
- Commit often with clear, descriptive messages
- Regularly sync your branch with main to avoid conflicts
- Write documentation for your prototypes
- Test thoroughly before creating a Pull Request

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.