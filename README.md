# 💁 Brag AI

Generate and maintain a brag document automatically from your GitHub contributions, powered by AI.

Because your awesome work deserves to be remembered! ✨

## Overview

Ever had that moment when your manager asks "So, what have you been up to?" and your mind goes blank?

Brag AI is your personal achievement historian! It helps you create and maintain a "brag document" - a fancy record of all the cool stuff you've done. It dives into your GitHub activity and transforms those cryptic commit messages into beautiful, human-readable achievements that will make your portfolio shine! ✨

Perfect for:

- 📊 Performance reviews (without the last-minute panic)
- 💼 Job applications (show off with style)
- 📈 Personal development tracking (watch yourself grow!)
- 🎉 Impressing your friends (and maybe your pet - results may vary)

## Features

- 🔍 **GitHub Integration**: Automagically analyzes your commits to generate achievement descriptions
- 🤖 **AI-Powered**: Turns "fix: bug in login" into "Enhanced system reliability by resolving critical authentication issues"
- 💻 **CLI Tool**: Easy to use command-line interface

## Installation

This project is still not published to PyPI. You can install it from source using pip:

```console
pip install git+https://github.com/ruancomelli/brag-ai.git
```

If you use [`uv`](https://docs.astral.sh/uv/), you can also run this tool using
`uvx` tool calling:

```console
uvx --from git+https://github.com/ruancomelli/brag-ai brag --help # or any other command
```

## Usage

### Generate a brag document from a GitHub repository

```console
brag owner/repo --user github-username
```

### Options

- `--user`: The GitHub username to generate the brag document for. If not provided, the owner of the GitHub API token will be used.
- `--from`: The start date to generate the brag document for (format: YYYY-MM-DD).
- `--to`: The end date to generate the brag document for (format: YYYY-MM-DD).
- `--limit`: The maximum number of commits to include in the brag document.
- `--github-api-token`: The GitHub API token to use for authentication. If not provided, only public information will be included.
- `--output`: The path to save the generated brag document. If not specified, the document will be printed to stdout.
- `--overwrite`: If set, overwrites the output file if it already exists.
- `--model`: The name of the AI model to use for generating the brag document.
- `--language`: The language to use for generating the brag document.

### Example

```console
# Generate a brag document for the user `my-username` from their contributions
# to `my-org/my-repo`
brag my-org/my-repo --user my-username \
  # only consider contributions from 2023-01-01 to 2023-12-31
  --from 2023-01-01 --to 2023-12-31 \
  # generate the brag document in Portuguese
  --language Português \
  # save the brag document to the file `brag.md`
  --output brag.md
```

### Choosing different models

Brag AI uses `pydantic-ai` under the hood, and hence supports [all models
supported by them](https://ai.pydantic.dev/models/).

A model can be picked by passing the `--model` argument when executing `brag`.
Model API keys are provided by setting environment variables according to
[`pydantic-ai`'s nomenclature](https://ai.pydantic.dev/models/):

```console
# Use OpenAI's GPT-4o
export OPENAI_API_KEY=your-openai-api-key
brag --model openai:gpt-4o owner/repo --user github-username
# Use Anthropic's Claude
export ANTHROPIC_API_KEY=your-anthropic-api-key
brag --model anthropic:claude-3-5-sonnet-latest owner/repo --user github-username
# Use Google's Gemini
export GEMINI_API_KEY=your-gemini-api-key
brag --model google-vertex:gemini-2.0-flash owner/repo --user github-username
```

### Full API

For more details, use the `--help` flag:

```console
brag --help
```

## Coming Soon™ 🚀

- 🌐 **Web Interface**: Because sometimes clicking is better than typing
- 🤝 **Extended GitHub Integration**: Support for PR reviews, issues, and discussions
- 🔄 **Integration with other tools**: GitLab, Bitbucket, and more - we don't discriminate!
- 📝 **Custom Templates**: Make your brag document as unique as you are
- 📦 **Export Options**: More ways to show off your achievements (JSON brag documents anyone?)
- 🔒 **Local Processing**: Your precious data stays on your machine if you use local LLMs

## Contributing

Got ideas? We'd love to hear them! Check out our [Contributing Guide](CONTRIBUTING.md) to join the fun! 🎈

## License

<!-- TODO: switch to MIT -->

This project is currently private (shhh... 🤫)

## Support

- 📖 [Documentation](https://github.com/ruancomelli/brag-ai/blob/main/README.md)
- 🐛 [Issue Tracker](https://github.com/ruancomelli/brag-ai/issues)
- 💬 [Discussions](https://github.com/ruancomelli/brag-ai/discussions)
- 💻 [Repository](https://github.com/ruancomelli/brag-ai)

## Why Brag AI?

Maintaining a brag document is crucial for career development, but it's often overlooked or forgotten until it's time for a performance review.
Brag AI automates this process, helping you capture your achievements while they're fresh or after a long time.

---

Built with ❤️ and ☕ by [Ruan Comelli](https://github.com/ruancomelli)

_Remember: It's not bragging if it's true! ✨_
