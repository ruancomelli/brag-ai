# Installation

There are several ways to install Brag AI. Choose the one that best suits your needs.

## Using [`uv`](https://docs.astral.sh/uv/) (Recommended)

The easiest way to install Brag AI is using [`uv`](https://docs.astral.sh/uv/):

```bash
uv tool install brag-ai
```

After installation, you can verify it worked by running:

```bash
brag --version
```

## Using [`pipx`](https://pipx.pypa.io/stable/)

If you prefer using `pipx`, you can install Brag AI with:

```bash
pipx install brag-ai
```

## Using `pip`

If you prefer using `pip`, you can install Brag AI with:

```bash
pip install brag-ai
```

However, please note that this will install `brag-ai` into your global Python environment, which might not be what you want.
Make sure to use a [virtual environment](https://docs.python.org/3/library/venv.html) to install Brag AI if you don't want to have it installed globally.

## Requirements

- Python 3.12 or higher
- A GitHub account (for accessing repositories)
- An LLM provider API key (for AI processing)

## Environment Setup

After installation, you'll need to set up your environment:

1. (Optional) Get your GitHub Personal Access Token:

   - Go to GitHub Settings > Developer Settings > Personal Access Tokens
   - Create a new token with `repo` scope
   - Save the token securely (e.g. add `GITHUB_API_TOKEN=<your-token>` to a `.env` file)
   - This step is optional - if you don't provide a GitHub token, the brag document will only include public information

2. Get your LLM provider API key:

   - Sign up for an LLM provider account if you haven't already
   - Create a new API key
   - Save the key securely

3. Set up your environment variables:

```bash
export GITHUB_API_TOKEN="your-github-token"
# Then, depending on the LLM provider you're using, set the following environment variables:
export OPENAI_API_KEY="your-openai-api-key"
export GEMINI_API_KEY="your-gemini-api-key"
export ANTHROPIC_API_KEY="your-anthropic-api-key"
```

You can also add these to your `.bashrc`, `.zshrc`, or equivalent shell configuration file for persistence.

## Verifying Installation

To verify everything is set up correctly:

```bash
# Check the installed version
brag --version

# Run a test command
brag --help
```

If you see the help message and version information, you're ready to start using Brag AI!

## Next Steps

- Read the [Usage Guide](usage.md) to learn how to use Brag AI
- Check out the [Configuration Options](configuration.md) to customize your experience
