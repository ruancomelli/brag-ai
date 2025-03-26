# 💁 Brag AI

[![PyPI](https://img.shields.io/pypi/v/brag-ai.svg?logo=pypi&logoColor=white)](https://pypi.org/project/brag-ai)
[![Python Version](https://img.shields.io/pypi/pyversions/brag-ai.svg?logo=python&logoColor=yellow)](https://python.org)
[![Docs](https://img.shields.io/badge/docs-latest-blue)](https://www.ruancomelli.com/brag-ai/)

[![uv-managed](https://img.shields.io/badge/managed-261230?label=uv&logo=uv&labelColor=gray)](https://github.com/astral-sh/uv)
[![CI](https://github.com/ruancomelli/brag-ai/actions/workflows/ci.yaml/badge.svg)](https://github.com/ruancomelli/brag-ai/actions/workflows/ci.yaml)
[![Codecov](https://codecov.io/gh/ruancomelli/brag-ai/branch/main/graph/badge.svg)](https://codecov.io/gh/ruancomelli/brag-ai)
[![Sourcery](https://img.shields.io/badge/Sourcery-enabled-orange?logo=hackthebox&logoColor=orange)](https://sourcery.ai)
[![Code style: Ruff](https://img.shields.io/badge/Ruff-checked-261230.svg?logo=ruff)](https://docs.astral.sh/ruff/)
[![Pydantic v2](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pydantic/pydantic/main/docs/badge/v2.json)](https://pydantic.dev)

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![SemVer](https://img.shields.io/badge/semver-2.0.0-green)](https://semver.org/spec/v2.0.0.html)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org)
[![Author: ruancomelli](https://img.shields.io/badge/ruancomelli-blue?style=flat&label=author)](https://github.com/ruancomelli)

Generate and maintain a brag document automatically from your GitHub contributions, powered by AI.

Because your awesome work deserves to be remembered! ✨

<p align="center">
<a href="docs/assets/hero.png">
<img
  src=docs/assets/hero.png
  alt="Brag AI Hero"
  width="300"
  align="center"
>
</a>
</p>

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

Install `brag-ai` using `uv`, `pipx` or `pip`:

```console
# Install the package
uv tool install brag-ai
# or
# pipx install brag-ai
# or
# pip install brag-ai

# Generate a brag document from a GitHub repository
brag from-repo owner/repo --user github-username
```

If you use [`uv`](https://docs.astral.sh/uv/), you can also install and run this tool in one go using the `uvx` tool:

```console
uvx --from brag-ai brag from-repo owner/repo --user github-username
```

The final step is then: ⭐ star [this repo](https://github.com/ruancomelli/brag-ai)!

## Documentation

For detailed instructions, please refer to the documentation:

- [Installation Guide](https://www.ruancomelli.com/brag-ai/installation/)
- [Usage Guide](https://www.ruancomelli.com/brag-ai/usage/)
- [Configuration Options](https://www.ruancomelli.com/brag-ai/configuration/)
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

This project is licensed under the [GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/) - see the [LICENSE](LICENSE) file for details.

## Support

- 📖 [Documentation](https://www.ruancomelli.com/brag-ai/)
- 🐛 [Issue Tracker](https://github.com/ruancomelli/brag-ai/issues)
- 💬 [Discussions](https://github.com/ruancomelli/brag-ai/discussions)
- 💻 [Repository](https://github.com/ruancomelli/brag-ai.git)

## Why Brag AI?

Maintaining a brag document is crucial for career development, but it's often overlooked or forgotten until it's time for a performance review.
Brag AI automates this process, helping you capture your achievements while they're fresh or after a long time.

---

Built with ❤️ and ☕ by [Ruan Comelli](https://github.com/ruancomelli)

_Remember: It's not bragging if it's true! ✨_
