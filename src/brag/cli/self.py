"""The `self` subcommand of the `brag` CLI."""

import subprocess
import sys

from cyclopts import App

from brag import __version__ as CURRENT_BRAG_VERSION

app = App(
    name="self",
    help="Manage the `brag-ai` CLI itself.",
)


@app.command
def upgrade() -> None:
    """Update brag to latest stable version."""
    # Implementation based on the `cyclopts` cookbook example:
    # https://cyclopts.readthedocs.io/en/latest/cookbook/app_upgrade.html

    old_version = CURRENT_BRAG_VERSION

    subprocess.check_output(
        (sys.executable, "-m", "pip", "install", "--upgrade", "brag")
    )

    res = subprocess.run(
        (sys.executable, "-m", "brag", "--version"),
        stdout=subprocess.PIPE,
        check=True,
    )
    new_version = res.stdout.decode().strip()

    if old_version != new_version:
        print(f"`brag-ai` updated from v{old_version} to v{new_version}.")
    else:
        print(f"`brag-ai` is already up-to-date (v{new_version}).")
