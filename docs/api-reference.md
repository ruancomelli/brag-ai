# API Reference

This guide provides details about the key modules and functions in the Brag AI codebase. It's useful if you want to use Brag AI programmatically or extend its functionality.

## Core Modules

### `brag.__main__`

The entry point for the Brag AI CLI application.

```python
from brag.__main__ import app

# Run the CLI app
app()
```

### `brag.cli`

Contains the command-line interface implementation using Typer.

```python
from brag.cli import app

# Access the Typer app
app.info
```

### `brag.github_commits`

Provides functionality for retrieving commits from GitHub repositories.

```python
from brag.github_commits import get_commits_for_user

# Get commits for a user in a repository
commits = get_commits_for_user(
    repo_name="owner/repo",
    username="github-username",
    token="github-api-token",
    from_date="2023-01-01",
    to_date="2023-12-31",
    limit=50
)
```

### `brag.agents`

Contains AI agent implementations for generating brag documents.

```python
from brag.agents import BragDocumentGenerator

# Create a brag document generator
generator = BragDocumentGenerator(
    model="openai:gpt-4o",
    language="English"
)

# Generate a brag document from commits
brag_document = generator.generate_brag_document(commits)
```

### `brag.repository`

Provides abstractions for working with Git repositories.

```python
from brag.repository import Repository

# Create a repository instance
repo = Repository.from_name("owner/repo", token="github-api-token")
```

### `brag.text_formatters`

Contains utilities for formatting text output.

```python
from brag.text_formatters import markdown_formatter

# Format text as markdown
formatted_text = markdown_formatter("# Heading\n\nParagraph")
```

## Key Classes and Functions

### `BragDocumentGenerator`

The main class for generating brag documents.

```python
from brag.agents import BragDocumentGenerator

generator = BragDocumentGenerator(
    model="openai:gpt-4o",
    language="English"
)

brag_document = generator.generate_brag_document(commits)
```

#### Parameters

- `model`: The name of the AI model to use for generating the brag document.
- `language`: The language to use for generating the brag document.

#### Methods

- `generate_brag_document(commits)`: Generates a brag document from a list of commits.

### `get_commits_for_user`

Function to retrieve commits for a specific user in a repository.

```python
from brag.github_commits import get_commits_for_user

commits = get_commits_for_user(
    repo_name="owner/repo",
    username="github-username",
    token="github-api-token",
    from_date="2023-01-01",
    to_date="2023-12-31",
    limit=50
)
```

#### Parameters

- `repo_name`: The name of the repository (in the format "owner/repo").
- `username`: The GitHub username to get commits for.
- `token`: The GitHub API token for authentication (optional).
- `from_date`: The start date to get commits from (format: YYYY-MM-DD).
- `to_date`: The end date to get commits to (format: YYYY-MM-DD).
- `limit`: The maximum number of commits to retrieve.

### `Repository`

Class for working with Git repositories.

```python
from brag.repository import Repository

repo = Repository.from_name("owner/repo", token="github-api-token")
```

#### Class Methods

- `from_name(repo_name, token=None)`: Creates a Repository instance from a repository name.

## Usage Examples

### Generating a Brag Document Programmatically

```python
from brag.github_commits import get_commits_for_user
from brag.agents import BragDocumentGenerator

# Get commits for a user
commits = get_commits_for_user(
    repo_name="owner/repo",
    username="github-username",
    token="github-api-token",
    from_date="2023-01-01",
    to_date="2023-12-31"
)

# Generate a brag document
generator = BragDocumentGenerator(model="openai:gpt-4o")
brag_document = generator.generate_brag_document(commits)

# Print or save the brag document
print(brag_document)
# Or
with open("brag.md", "w") as f:
    f.write(brag_document)
```

### Using Custom Formatters

```python
from brag.github_commits import get_commits_for_user
from brag.agents import BragDocumentGenerator
from brag.text_formatters import markdown_formatter

# Get commits
commits = get_commits_for_user(repo_name="owner/repo", username="github-username")

# Generate brag document
generator = BragDocumentGenerator()
brag_document = generator.generate_brag_document(commits)

# Format the brag document
formatted_document = markdown_formatter(brag_document)

# Save the formatted document
with open("brag.md", "w") as f:
    f.write(formatted_document)
```

## Error Handling

When using the Brag AI API, you might encounter various errors. Here's how to handle them:

```python
from brag.github_commits import get_commits_for_user
import github.GithubException

try:
    commits = get_commits_for_user(repo_name="owner/repo", username="github-username")
except github.GithubException as e:
    if e.status == 404:
        print("Repository or user not found")
    elif e.status == 401:
        print("Authentication failed, check your token")
    else:
        print(f"GitHub API error: {e}")
except Exception as e:
    print(f"Error: {e}")
```
