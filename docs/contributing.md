# Contributing to Brag AI 🎈

So you want to contribute to Brag AI? Awesome! We're thrilled to have you join our quest to make bragging (about
your achievements) an automated art form. Here's how you can help:

## Getting Started

1.  **Fork the repository**: Click the "Fork" button at the top right of the [GitHub repository](https://github.com/ruancomelli/brag-ai).
2.  **Clone your fork**:

    ```bash
    git clone https://github.com/your-username/brag-ai.git
    cd brag-ai
    ```

3.  **Set up your development environment**: We use `uv` to manage our dependencies. Initialize your environment with:

    ```bash
    bash scripts/init.sh
    ```

    This will:

    - Install all the required dev dependencies; and
    - Set up pre-commit hooks

4.  **Create a branch**:

    ```bash
    git checkout -b your-awesome-feature-name
    ```

## Making Changes

1.  **Make your changes**: Go wild! But please, keep the code clean and well-documented.
2.  **Test your changes**: Run the tests to make sure you haven't broken anything:

    ```bash
    bash scripts/test.sh
    ```

    To run tests with coverage:

    ```bash
    bash scripts/test-cov.sh
    ```

3.  **Format your code**: Keep the code style consistent by running:

    ```bash
    bash scripts/format.sh
    ```

4.  **Lint your code**: Catch those pesky little errors with:

    ```bash
    bash scripts/lint.sh
    ```

5.  **Type-check your code**: Ensure type correctness by running:

    ```bash
    bash scripts/type-check.sh
    ```

6.  **Commit your changes**:

    ```bash
    git add .
    git commit -m "feat: Add your awesome feature"
    ```

    Make sure your commit messages follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0) format.

7.  **Push to your fork**:

    ```bash
    git push origin your-awesome-feature-name
    ```

## Submitting a Pull Request

1.  **Create a pull request**: Go to your fork on GitHub and click the "Create Pull Request" button.
2.  **Describe your changes**: Provide a clear and concise description of your changes.
3.  **Wait for review**: Our team will review your pull request and provide feedback.
4.  **Address feedback**: Make any necessary changes based on the feedback.
5.  **Get merged!**: Once your pull request is approved, it will be merged into the main branch. Congratulations,
    you're now a Brag AI contributor! 🎉

## Useful Scripts

We have a few utility scripts in the `scripts/` directory to help you with development:

- `scripts/init.sh`: Initializes the development environment by installing dependencies and setting up pre-commit hooks.
- `scripts/test.sh`: Runs the tests. If invoked without arguments, it runs all tests. If invoked with test names, it runs only those tests.
- `scripts/test-cov.sh`: Runs the tests with coverage.
- `scripts/format.sh`: Formats the code. If invoked without arguments, it formats the entire codebase. If invoked with file paths, it formats only those files.
- `scripts/lint.sh`: Lints the code. If invoked without arguments, it lints the entire codebase. If invoked with file paths, it lints only those files.
- `scripts/type-check.sh`: Type-checks the code. If invoked without arguments, it type-checks the entire codebase. If invoked with file paths, it type-checks only those files.

## Contributing to Documentation

If you want to contribute to the documentation, you'll need to set up MkDocs:

1. **Install MkDocs and the required dependencies**:

   ```bash
   uv add --group docs mkdocs mkdocs-material pymdown-extensions
   ```

2. **Make your changes** to the Markdown files in the `docs/` directory.

3. **Preview your changes** by running the MkDocs development server:

   ```bash
   uv run --group docs mkdocs serve
   ```

4. **Build the documentation** to verify that it builds successfully:

   ```bash
   uv run --group docs mkdocs build --strict
   ```

5. **Commit and push your changes** as normal.

## Code Style Guidelines

We follow these general guidelines for code style:

- Use [ruff](https://github.com/astral-sh/ruff) for linting and formatting
- Follow [PEP 8](https://peps.python.org/pep-0008/) style guidelines
- Use type hints for all function parameters and return values
- Write docstrings for all modules, classes, and functions
- Use [Conventional Commits](https://www.conventionalcommits.org/) for commit messages

## Have Fun!

We're all here to learn and grow together. Don't be afraid to ask questions, experiment, and have fun! ✨
However, keep in mind that we're all volunteers, so please be patient and respectful when waiting for feedback.
It is also of utmost importance to be respectful - treat others as you would like to be treated.
