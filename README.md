# 💁 Brag AI

Because your awesome work deserves to be remembered! ✨

Generate and maintain a brag document automatically from your GitHub contributions, powered by AI.

## Overview

Ever had that moment when your manager asks "So, what have you been up to?" and your mind goes blank? 🤔

Brag AI is your personal achievement historian! It helps you create and maintain a "brag document" - a fancy record of all the cool stuff you've done. It dives into your GitHub activity and transforms those cryptic commit messages into beautiful, human-readable achievements that'll make your portfolio shine! ✨

Perfect for:

- 📊 Performance reviews (without the last-minute panic)
- 💼 Job applications (show off with style)
- 📈 Personal development tracking (watch yourself grow!)
- 🎉 Impressing your friends (and maybe your cat - results may vary)

## Features

- 🔍 **GitHub Integration**: Automagically analyzes your commits to generate achievement descriptions
- 🤖 **AI-Powered**: Turns "fix bug in login" into "Enhanced system reliability by resolving critical authentication issues"
- 💻 **CLI Tool**: Easy to use command-line interface

## Installation

```console
pip install brag-ai
```

## Usage

### Basic Usage

Let's make you look good! Generate a brag document from your recent GitHub activity:

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

## Coming Soon™ 🚀

- 🌐 **Web Interface**: Because sometimes clicking is better than typing
- 🤝 **Extended GitHub Integration**: Support for PR reviews, issues, and discussions
- 🔄 **Integration with other tools**: GitLab, Bitbucket, and more - we don't discriminate!
- 📝 **Custom Templates**: Make your brag document as unique as you are
- 📦 **Export Options**: More ways to show off your achievements
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

## Why Brag AI?

Maintaining a brag document is crucial for career development, but it's often overlooked or forgotten until it's time for a performance review.
Brag AI automates this process, helping you capture your achievements while they're fresh or after a long time.

---

Built with ❤️ and ☕ by [Ruan Comelli](https://github.com/ruancomelli)

_Remember: It's not bragging if it's true! ✨_
