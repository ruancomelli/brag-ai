# 💁 Brag AI

Generate and maintain a brag document automatically from your GitHub contributions, powered by AI.

Because your awesome work deserves to be remembered! ✨

<h1 align="center">
<a href="docs/assets/hero.webp">
<img
  src=docs/assets/hero.webp
  alt="Brag AI Hero"
  width="300"
  align="center"
>
</a>
</h1>

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

## Quick Start

This project is still not published to PyPI. You can install it from source using pip:

```console
# Install the package
pip install git+https://github.com/ruancomelli/brag-ai.git

# Generate a brag document from a GitHub repository
brag owner/repo --user github-username
```

If you use [`uv`](https://docs.astral.sh/uv/), you can also run this tool using
`uvx` tool calling:

```console
uvx --from git+https://github.com/ruancomelli/brag-ai brag --help # or any other command
```

## Documentation

For detailed instructions, please refer to the documentation:

- [Installation Guide](https://ruancomelli.github.io/brag-ai/installation/)
- [Usage Guide](https://ruancomelli.github.io/brag-ai/usage/)
- [Configuration Options](https://ruancomelli.github.io/brag-ai/configuration/)
- [API Reference](https://ruancomelli.github.io/brag-ai/api-reference/)
- [Development Guide](https://github.com/ruancomelli/brag-ai/blob/main/CONTRIBUTING.md)

## Coming Soon™ 🚀

- 🌐 **Web Interface**: Because sometimes clicking is better than typing
- 🤝 **Extended GitHub Integration**: Support for PR reviews, issues, and discussions
- 🔄 **Integration with other tools**: GitLab, Bitbucket, and more
- 📝 **Custom Templates**: Make your brag document as unique as you are
- 📦 **Export Options**: More ways to show off your achievements (JSON brag documents anyone?)
- 🔒 **Local Processing**: Your precious data stays on your machine if you use local LLMs

## Contributing

Got ideas? We'd love to hear them! Check out our [Contributing Guide](CONTRIBUTING.md) to join the fun! 🎈

## License

<!-- TODO: switch to MIT -->

This project is currently private (shhh... 🤫)

## Support

- 📖 [Documentation](https://ruancomelli.github.io/brag-ai/)
- 🐛 [Issue Tracker](https://github.com/ruancomelli/brag-ai/issues)
- 💬 [Discussions](https://github.com/ruancomelli/brag-ai/discussions)
- 💻 [Repository](https://github.com/ruancomelli/brag-ai)

## Why Brag AI?

Maintaining a brag document is crucial for career development, but it's often overlooked or forgotten until it's time for a performance review.
Brag AI automates this process, helping you capture your achievements while they're fresh or after a long time.

---

Built with ❤️ and ☕ by [Ruan Comelli](https://github.com/ruancomelli)

_Remember: It's not bragging if it's true! ✨_
