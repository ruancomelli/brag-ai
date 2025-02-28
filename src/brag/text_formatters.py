"""Utilities for formatting text."""

import textwrap


def promptify(*blocks: str | None, joiner: str = "\n\n") -> str:
    """Compose a text from multiple building blocks.

    All building blocks get formatted in advance to ensure that the result text has consistent indentation.
    """
    return joiner.join(_dedent_triple_quote_string(block) for block in blocks if block)


def _dedent_triple_quote_string(text: str | None) -> str:
    """Dedent a triple quote string.

    This allows us to write multi-line strings with consistent indentation:
    ```python
    foo = '''
        <text>
    '''
    ```
    instead of:
    ```python
    foo = '''
    <text>
    '''
    ```
    """
    if not text:
        return ""
    return textwrap.dedent(text).strip()
