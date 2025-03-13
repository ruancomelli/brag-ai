# Usage Guide

Brag AI is designed to be simple to use while providing powerful functionality. This guide will walk you through the basic and advanced usage of the tool.

## Basic Usage

### From a remote GitHub repository

The primary use case is to generate a brag document for your contributions to a specific GitHub repository:

```bash
brag from-repo \
  --repo my-org/my-repo \
  --user my-username
```

You can also specify a GitHub repository using its URL:

```bash
brag from-repo \
  --repo https://github.com/my-org/my-repo \
  --user my-username
```

This is convenient when copying a repository URL directly from a browser.

### From a local Git repository

If you want to generate a brag document from a local Git repository instead of a remote GitHub repository, you can use the `from-local` command:

```bash
brag from-local \
  /path/to/local/repo \
  --user my-username
```

This command is particularly useful when:

- You have a private repository that you've already cloned locally
- You're working with repositories hosted on platforms other than GitHub
- You want to avoid GitHub API rate limits
- You need faster processing since it reads directly from your local filesystem

Note that this option requires you to have the repository cloned on your machine first, as it reads the Git history directly from your local filesystem.

## Command Line Options

Brag AI offers several command line options to customize the generated brag document:

| Option                                | Description                                                                                                                                            |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `--repo` (`owner/repo` or GitHub URL) | The repository to generate the brag document for. Can be in `owner/repo` format or a GitHub URL. (Used with `from-repo`)                               |
| `--repo` Path argument                | The path to a local Git repository (used with `from-local`).                                                                                           |
| `--user`                              | The GitHub username or Git author to generate the brag document for. If not provided with `from-repo`, the owner of the GitHub API token will be used. |
| `--from`                              | The start date to generate the brag document for (format: YYYY-MM-DD).                                                                                 |
| `--to`                                | The end date to generate the brag document for (format: YYYY-MM-DD).                                                                                   |
| `--limit`                             | The maximum number of commits to include in the brag document.                                                                                         |
| `--input`, `--i`                      | Path to an existing brag document to update with new contributions. If not provided, a new brag document will be generated from scratch.               |
| `--on-missing-input`                  | What to do if the input brag document does not exist. Options: `error` (default) or `ignore`.                                                          |
| `--github-api-token`                  | The GitHub API token to use for authentication (only for `from-repo`). If not provided, only public information will be included.                      |
| `--output`, `-o`                      | The path to save the generated brag document. If not specified, the document will be printed to stdout.                                                |
| `--on-existing-output`                | What to do if the output file already exists. Options: `error` (default) or `overwrite`.                                                               |
| `--model`                             | The name of the AI model to use for generating the brag document.                                                                                      |
| `--language`                          | The language to use for generating the brag document.                                                                                                  |

## Examples

Here are some examples of how to use Brag AI in different scenarios:

### Generate a Brag Document for a Specific Time Period

```bash
brag from-repo my-org/my-repo --user my-username --from 2023-01-01 --to 2023-12-31
```

This will generate a brag document for the user `my-username` based on their contributions to the `my-org/my-repo` repository between January 1, 2023, and December 31, 2023.

### Generate a Brag Document from a Local Repository

```bash
brag from-local ~/projects/my-project --user my-username --from 2023-01-01 --to 2023-12-31
```

This will generate a brag document for the user `my-username` based on their contributions to the local repository at `~/projects/my-project` between January 1, 2023, and December 31, 2023.

### Generate a Brag Document in a Different Language

```bash
brag from-repo my-org/my-repo --user my-username --language Português
```

This will generate a brag document in Portuguese.

### Save the Brag Document to a File

```bash
brag from-repo \
  --repo my-org/my-repo \
  --user my-username \
  --output brag.md
```

This will save the generated brag document to a file named `brag.md`.

### Combine Multiple Options

```bash
brag from-repo \
  --repo my-org/my-repo \
  --user my-username \
  --from 2023-01-01 \
  --to 2023-12-31 \
  --language Português \
  --output brag.md
```

This combines multiple options to generate a brag document in Portuguese for a specific time period and save it to a file.

### Update an Existing Brag Document

```bash
brag from-repo \
  --repo my-org/my-repo \
  --user my-username \
  --input existing-brag.md \
  --output updated-brag.md
```

This will update an existing brag document (`existing-brag.md`) with new contributions from the repository, and save the result to `updated-brag.md`.

You can also update your brag document incrementally using the same output file:

```bash
brag from-repo \
  --repo my-org/my-repo \
  --user my-username \
  --input brag.md \
  --output brag.md \
  --on-existing-output overwrite
```

This will read the existing brag document, update it with new contributions, and overwrite the same file.

## Using Different AI Models

Brag AI supports various AI models through [PydanticAI](https://ai.pydantic.dev/models/). You can specify which model to use with the `--model` option:

### OpenAI Models

```bash
export OPENAI_API_KEY=your-openai-api-key
brag from-repo owner/repo --model openai:gpt-4o --user github-username
```

### Anthropic Models

```bash
export ANTHROPIC_API_KEY=your-anthropic-api-key
brag from-repo owner/repo --model anthropic:claude-3-5-sonnet-latest --user github-username
```

### Google Models

```bash
export GEMINI_API_KEY=your-gemini-api-key
brag from-repo owner/repo --model google-vertex:gemini-2.0-flash --user github-username
```

## Viewing Help Information

For a complete list of commands and options, use the `--help` flag:

```bash
brag --help
```
