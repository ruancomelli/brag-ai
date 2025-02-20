# Brag AI

Generate and maintain a brag document automatically from your GitHub contributions, powered by AI.

## Overview

Brag AI helps you create and maintain a "brag document" - a record of your professional achievements and contributions. It analyzes your GitHub activity and generates meaningful descriptions of your work that you can use for performance reviews, job applications, or personal development tracking.

## Features

- **GitHub Integration**: Automatically analyzes your commits to generate achievement descriptions
- **AI-Powered**: Converts technical contributions into clear, impactful statements
- **CLI Tool**: Easy to use command-line interface
- **Customizable Output**: Generate documents in various formats
- **Local Processing**: Your data stays on your machine

## Installation

```console

```

## Usage

### Basic Usage

Generate a brag document from your recent GitHub activity:

```console
brag generate --user <github-username>
```

### Options

#### Generate for a specific time period

```console
brag generate --from 2024-01-01 --to 2024-03-31
```

#### Focus on specific repositories

```console
brag generate --repo repo1 --repo repo2
```

#### Export in different formats

```console
brag generate --format markdown
brag generate --format json
```

The brag document is a JSON object with the following structure:

<!-- TODO: Add JSON schema -->

```json

```

### Full API

<!-- TODO: post the CLI `--help` menus here -->

## Coming Soon

- **Web Interface**: Access Brag AI through a user-friendly website
- **Extended GitHub Integration**: Support for PR reviews, issues, and discussions
- **Integration with other tools**: Support for other tools like GitLab, Bitbucket etc.
- **Custom Templates**: Create your own formats for brag documents
- **Export Options**: Additional export formats

## Contributing

Contributions are welcome! Please check out our [Contributing Guide](CONTRIBUTING.md) for guidelines.

## License

<!-- TODO: switch to MIT -->

This project is currently private.

## Support

<!-- TODO: add docs -->

- 📖 [Documentation](https://github.com/ruancomelli/brag-ai/blob/main/README.md)
- 🐛 [Issue Tracker](https://github.com/ruancomelli/brag-ai/issues)
- 💬 [Discussions](https://github.com/ruancomelli/brag-ai/discussions)

## Why Brag AI?

Maintaining a brag document is crucial for career development, but it's often overlooked or forgotten until it's time for a performance review.
Brag AI automates this process, helping you capture your achievements while they're fresh or after a long time.

---

Built with ❤️ by [Ruan Comelli](https://github.com/ruancomelli)
