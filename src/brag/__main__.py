"""Entry point for the brag command-line interface.

This module serves as the entry point for the brag command-line interface.
It imports the `app` function from the `brag.cli` module and calls it when the script is executed directly.
"""

from brag.cli import app

if __name__ == "__main__":
    app()
