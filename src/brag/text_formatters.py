import textwrap


def dedent_triple_quote_string(text: str | None) -> str:
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


def compose_text(*blocks: str, joiner: str = "\n\n") -> str:
    """Compose a text from multiple building blocks.

    All building blocks get formatted in advance to ensure that the result text has consistent indentation.
    """
    formatted_blocks = [dedent_triple_quote_string(block) for block in blocks if block]
    return joiner.join(formatted_blocks)
