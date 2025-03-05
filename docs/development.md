# Development Guide

This guide explains how to set up your development environment, understand the project structure, and contribute to the Brag AI codebase.

## Project Structure

The Brag AI project is organized as follows:

```
brag-ai/
├── docs/                  # Documentation files
├── scripts/               # Development utility scripts
├── src/                   # Source code
│   └── brag/              # Main package
│       ├── __init__.py    # Package initialization
│       ├── __main__.py    # CLI entry point
│       ├── agents.py      # AI agent implementations
│       ├── cli.py         # Command-line interface
│       ├── github_commits.py  # GitHub API interactions
│       ├── repository.py  # Repository abstractions
│       └── text_formatters.py # Text formatting utilities
├── tests/                 # Test files
├── .env                   # Environment variables
├── .gitignore             # Git ignore file
├── .pre-commit-config.yaml # Pre-commit hooks configuration
├── pyproject.toml         # Project configuration
└── README.md              # Project README
```

## Development Environment Setup

### Prerequisites

- Python 3.12 or higher
- [uv](https://docs.astral.sh/uv/) (recommended for dependency management)
- Git

### Setting Up Your Environment

1. **Clone the repository**:

   ```bash
   git clone https://github.com/ruancomelli/brag-ai.git
   cd brag-ai
   ```

2. **Initialize the development environment**:

   ```bash
   bash scripts/init.sh
   ```

   This script:

   - Creates a virtual environment
   - Installs development dependencies
   - Sets up pre-commit hooks

3. **Set up environment variables**:

   Create a `.env` file in the project root:

   ```
   GITHUB_API_TOKEN=your_github_token
   OPENAI_API_KEY=your_openai_key
   ```

   This file is listed in `.gitignore` so you don't accidentally commit your tokens.

## Development Workflow

### Making Code Changes

1. **Create a branch**:

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**.

3. **Run tests to ensure your changes work**:

   ```bash
   bash scripts/test.sh
   ```

4. **Format your code**:

   ```bash
   bash scripts/format.sh
   ```

5. **Lint your code**:

   ```bash
   bash scripts/lint.sh
   ```

6. **Type-check your code**:

   ```bash
   bash scripts/type-check.sh
   ```

7. **Commit your changes using [Conventional Commits](https://www.conventionalcommits.org/) format**:

   ```bash
   git commit -m "feat: Add new feature"
   ```

8. **Push your changes**:

   ```bash
   git push origin feature/your-feature-name
   ```

9. **Open a pull request** on GitHub.

### Running the Application Locally

To run the application locally during development:

```bash
uv run src/brag/__main__.py --help
```

Or, if you've installed the package in development mode:

```bash
brag --help
```

## Testing

### Running Tests

Run all tests:

```bash
bash scripts/test.sh
```

Run specific tests:

```bash
bash scripts/test.sh tests/test_specific.py
```

Run tests with coverage:

```bash
bash scripts/test-cov.sh
```

This will generate a coverage report in the terminal and a `coverage.xml` file.

### Writing Tests

Tests are located in the `tests/` directory. We use pytest for testing.

When adding a new feature, please add corresponding tests. Aim for high test coverage and make sure to test edge cases.

Example test structure:

```python
# tests/test_feature.py
import pytest
from brag.feature import my_function

def test_my_function_happy_path():
    # Test normal operation
    result = my_function(input)
    assert result == expected

def test_my_function_edge_case():
    # Test edge case
    with pytest.raises(ValueError):
        my_function(bad_input)
```

## Documentation

### Updating Documentation

Documentation is built using MkDocs and the Material theme. Source files are in the `docs/` directory.

To preview documentation changes:

```bash
uv run --group docs mkdocs serve
```

This starts a local web server at http://127.0.0.1:8000/ where you can preview your changes.

To build the documentation:

```bash
uv run --group docs mkdocs build --strict
```

### Documentation Style Guide

- Use clear, concise language
- Include code examples where appropriate
- Format code blocks with syntax highlighting
- Use heading levels appropriately
- Include links to related documentation

## Code Style

We follow these style guidelines:

- Use [ruff](https://github.com/astral-sh/ruff) for linting and formatting
- Follow [PEP 8](https://peps.python.org/pep-0008/) style guidelines
- Use type hints for all function parameters and return values
- Write docstrings for all modules, classes, and functions
- Use descriptive variable and function names

## Debugging

### Logging

The application uses [loguru](https://github.com/Delgan/loguru) for logging. You can enable debug logs by setting the environment variable:

```bash
export LOGURU_LEVEL=DEBUG
```

### Debugging Tests

To debug tests with pytest, you can use the `-v` (verbose) flag:

```bash
pytest -v tests/test_feature.py
```

## CI/CD

The project uses GitHub Actions for continuous integration and deployment. The workflows are defined in the `.github/workflows/` directory.

The CI workflow runs on every pull request and checks:

- Code formatting
- Linting
- Type checking
- Test execution
- Documentation building

## Need Help?

If you're stuck or have questions, you can:

- Open an issue on GitHub
- Start a discussion in the GitHub Discussions section
- Check the existing documentation and issues for similar problems

## Tips and Tricks

- Use the development scripts in the `scripts/` directory to automate common tasks
- Keep PRs focused on a single feature or bug fix
- Add comments explaining complex logic
- Write tests before implementing features (TDD)
- Use descriptive commit messages to make the project history easier to understand
