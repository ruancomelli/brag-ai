# Configuration

Brag AI offers several configuration options to customize its behavior. This guide explains the different ways to configure Brag AI.

## Environment Variables

Brag AI supports the following environment variables:

### Authentication Tokens

| Environment Variable | Description                                                                                        |
| -------------------- | -------------------------------------------------------------------------------------------------- |
| `GITHUB_API_TOKEN`   | GitHub API token for authentication (required for private repositories or to increase rate limits) |
| `OPENAI_API_KEY`     | OpenAI API key for using OpenAI models                                                             |
| `ANTHROPIC_API_KEY`  | Anthropic API key for using Claude models                                                          |
| `GEMINI_API_KEY`     | Google API key for using Gemini models                                                             |

You can set these environment variables in your shell profile or use a `.env` file in your project directory.

Example `.env` file:

```
GITHUB_API_TOKEN=ghp_your_github_token
OPENAI_API_KEY=sk-your_openai_key
```

### Environment Variable Precedence

Environment variables take precedence over command-line arguments. For example, if you set `GITHUB_API_TOKEN` in your environment and also provide `--github-api-token` on the command line, the environment variable will be used.

## Command-Line Options

Brag AI has several command-line options that can be used to configure its behavior:

### Repository Selection

| Option       | Description                                                                    |
| ------------ | ------------------------------------------------------------------------------ |
| `owner/repo` | The GitHub repository to generate the brag document from (positional argument) |
| `--user`     | The GitHub username to generate the brag document for                          |

### Time Range

| Option    | Description                                                           |
| --------- | --------------------------------------------------------------------- |
| `--from`  | The start date to generate the brag document for (format: YYYY-MM-DD) |
| `--to`    | The end date to generate the brag document for (format: YYYY-MM-DD)   |
| `--limit` | The maximum number of commits to include in the brag document         |

### Authentication

| Option               | Description                                    |
| -------------------- | ---------------------------------------------- |
| `--github-api-token` | The GitHub API token to use for authentication |

### Output

| Option        | Description                                             |
| ------------- | ------------------------------------------------------- |
| `--output`    | The path to save the generated brag document            |
| `--overwrite` | If set, overwrites the output file if it already exists |

### AI Model Configuration

| Option       | Description                                                      |
| ------------ | ---------------------------------------------------------------- |
| `--model`    | The name of the AI model to use for generating the brag document |
| `--language` | The language to use for generating the brag document             |

## Model Selection

Brag AI supports a variety of AI models through `pydantic-ai`. You can specify which model to use with the `--model` option.

The format for the model name is `provider:model-name`. For example:

- `openai:gpt-4o`
- `anthropic:claude-3-5-sonnet-latest`
- `google-vertex:gemini-2.0-flash`

For a full list of supported models, see the [pydantic-ai documentation](https://ai.pydantic.dev/models/).

## Default Values

If not specified, Brag AI uses the following default values:

- User: The owner of the GitHub API token
- From date: None (no lower bound)
- To date: None (the current date)
- Limit: None (no limit)
- Output: stdout (print to console)
- Model: The default model configured in pydantic-ai
- Language: English

## Example Configurations

### Generate a brag document for contributions in 2023 using GPT-4o

```bash
export OPENAI_API_KEY=your-openai-api-key
brag from-repo owner/repo --user github-username --from 2023-01-01 --to 2023-12-31 --model openai:gpt-4o
```

### Generate a brag document in Portuguese using Claude

```bash
export ANTHROPIC_API_KEY=your-anthropic-api-key
brag from-repo owner/repo --user github-username --language Português --model anthropic:claude-3-5-sonnet-latest
```

### Save the brag document to a file and limit to the last 50 commits

```bash
brag from-repo owner/repo --user github-username --limit 50 --output brag.md
```
