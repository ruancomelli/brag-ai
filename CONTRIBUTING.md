# Contributing to Brag AI 🎈

So you want to contribute to Brag AI? Awesome! We're thrilled to have you join our quest to make bragging (about
your achievements) an automated art form. Here's how you can help:

## Getting Started

### Prerequisites

- The [uv](https://docs.astral.sh/uv/) package manager
- Git

### Setup

1. **Fork the repository**: Click the "Fork" button at the top right of https://github.com/ruancomelli/brag-ai.
2. **Clone your fork**:

   ```bash
   git clone https://github.com/your-username/brag-ai.git
   cd brag-ai
   ```

3. **Set up your development environment**: We use `uv` to manage our dependencies. Initialize your environment with:

   ```bash
   bash scripts/init.sh
   ```

   This will:

   - Install all the required dev dependencies; and
   - Set up pre-commit hooks

4. **Set up environment variables**:

   Create a `.env` file in the project root:

   ```
   GITHUB_API_TOKEN=your_github_token
   OPENAI_API_KEY=your_openai_key
   ```

   This file is listed in `.gitignore` so you don't accidentally commit your tokens.

5. **Create a branch**:

   ```bash
   git checkout -b your-awesome-feature-name
   ```

## Making Changes

1. **Make your changes**: Go wild! But please, keep the code clean and well-documented.

2. **Test your changes**: Run the tests to make sure you haven't broken anything:

   ```bash
   bash scripts/test.sh
   ```

   To run tests with coverage:

   ```bash
   bash scripts/test-cov.sh
   ```

3. **Format your code**: Keep the code style consistent by running:

   ```bash
   bash scripts/format.sh
   ```

4. **Lint your code**: Catch those pesky little errors with:

   ```bash
   bash scripts/lint.sh
   ```

5. **Type-check your code**: Ensure type correctness by running:

   ```bash
   bash scripts/type-check.sh
   ```

6. **Commit your changes**:

   ```bash
   git add .
   git commit -m "feat: Add your awesome feature"
   ```

   Make sure your commit messages follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0) format.

7. **Push to your fork**:

   ```bash
   git push origin your-awesome-feature-name
   ```

## Submitting a Pull Request

1. **Create a pull request**: Go to your fork on GitHub and click the "Create Pull Request" button.
2. **Describe your changes**: Provide a clear and concise description of your changes.
3. **Wait for review**: Our team will review your pull request and provide feedback.
4. **Address feedback**: Make any necessary changes based on the feedback.
5. **Get merged!**: Once your pull request is approved, it will be merged into the main branch. Congratulations,
   you're now a Brag AI contributor! 🎉

## Useful Scripts

We have a few utility scripts in the `scripts/` directory to help you with development:

- `scripts/init.sh`: Initializes the development environment by installing dependencies and setting up pre-commit hooks.
- `scripts/test.sh`: Runs the tests. If invoked without arguments, it runs all tests. If invoked with test names, it runs only those tests.
- `scripts/test-cov.sh`: Runs the tests with coverage.
- `scripts/format.sh`: Formats the code. If invoked without arguments, it formats the entire codebase. If invoked with file paths, it formats only those files.
- `scripts/lint.sh`: Lints the code. If invoked without arguments, it lints the entire codebase. If invoked with file paths, it lints only those files.
- `scripts/type-check.sh`: Type-checks the code. If invoked without arguments, it type-checks the entire codebase. If invoked with file paths, it type-checks only those files.

## Running the Application Locally

To run the application locally during development:

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

#### `tests/test_feature.py`

```python
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

## Contributing to Documentation

Documentation is built using MkDocs and the Material theme. Source files are in the `docs/` directory.

To preview documentation changes:

```bash
bash scripts/docs-serve.sh
```

This starts a local web server at http://127.0.0.1:8000/ where you can preview your changes.

To build the documentation:

```bash
bash scripts/docs-build.sh
```

### Documentation Style Guide

- Use clear, concise language
- Include code examples where appropriate
- Format code blocks with syntax highlighting
- Use heading levels appropriately
- Include links to related documentation

## Code Style Guidelines

We follow these general guidelines for code style:

- Use [ruff](https://github.com/astral-sh/ruff) for linting and formatting
- Use type hints for all function parameters and return values
- Write docstrings for all public modules, classes, and functions
- Use descriptive variable and function names
- Use [Conventional Commits](https://www.conventionalcommits.org/) for commit messages

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

## Have Fun!

We're all here to learn and grow together. Don't be afraid to ask questions, experiment, and have fun! ✨
However, keep in mind that we're all volunteers, so please be patient and respectful when waiting for feedback.
It is also of utmost importance to be respectful - treat others as you would like to be treated.
