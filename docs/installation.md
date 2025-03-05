# Installation

There are several ways to install Brag AI, depending on your needs and preferences.

## Requirements

- Python 3.12 or higher
- A GitHub account (for generating brag documents from GitHub repositories)
- An API key for at least one AI provider (OpenAI, Anthropic, or Google) if you want to use their models

## Installation Methods

### From Source (Recommended for Now)

This project is still not published to PyPI. You can install it from source using pip:

```bash
pip install git+https://github.com/ruancomelli/brag-ai.git
```

### Using `uv`

If you use [`uv`](https://docs.astral.sh/uv/), you can also run this tool using
`uvx` tool calling without installation:

```bash
uvx --from git+https://github.com/ruancomelli/brag-ai brag --help # or any other command
```

## Verifying Your Installation

To verify that Brag AI was installed correctly, run:

```bash
brag --version
```

You should see the current version number printed to the console.

## Setting Up API Keys

Brag AI uses `pydantic-ai` under the hood, which supports [various AI models](https://ai.pydantic.dev/models/).

To use these models, you'll need to set up API keys as environment variables:

### OpenAI

```bash
export OPENAI_API_KEY=your-openai-api-key
```

### Anthropic

```bash
export ANTHROPIC_API_KEY=your-anthropic-api-key
```

### Google (Gemini)

```bash
export GEMINI_API_KEY=your-gemini-api-key
```

You can set these environment variables in your shell profile or use a `.env` file in your project directory.

## GitHub Authentication

For accessing private GitHub repositories or increasing your rate limit, you can provide a GitHub API token:

```bash
export GITHUB_API_TOKEN=your-github-api-token
```

You can generate a Personal Access Token from your GitHub account settings. For more information, see GitHub's documentation on [Creating a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

## Next Steps

Now that you have Brag AI installed, check out the [Usage Guide](usage.md) to learn how to generate your first brag document!
