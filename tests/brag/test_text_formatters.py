import pytest

from brag.text_formatters import _dedent_triple_quote_string, promptify


@pytest.mark.parametrize(
    ("text", "expected"),
    (
        pytest.param(None, "", id="none"),
        pytest.param("", "", id="empty string"),
        pytest.param("Hello, world!", "Hello, world!", id="already dedented"),
        pytest.param(
            """
                Hello, world!
            """,
            "Hello, world!",
            id="main use case - single line",
        ),
        pytest.param(
            """
                Hello, world!
                Goodbye, world!
            """,
            "Hello, world!\nGoodbye, world!",
            id="main use case - multiline",
        ),
        pytest.param("  Hello, world!", "Hello, world!", id="leading spaces"),
        pytest.param(
            """
        Hello, world!
        """,
            "Hello, world!",
            id="weird indentation",
        ),
    ),
)
def test_dedent_triple_quote_string(
    text: str | None,
    expected: str,
) -> None:
    """Test dedent_triple_quote_string."""
    assert _dedent_triple_quote_string(text) == expected


@pytest.mark.parametrize(
    "blocks, expected",
    (
        pytest.param((), "", id="no blocks"),
        pytest.param(("", None, ""), "", id="empty blocks"),
        pytest.param(
            ("Hello, world!",),
            "Hello, world!",
            id="single block - already formatted",
        ),
        pytest.param(
            ("Hello, world!", "Goodbye, world!"),
            "Hello, world!\n\nGoodbye, world!",
            id="multiple blocks - already formatted",
        ),
        pytest.param(
            (
                """
                    Hello, world!
                    """,
            ),
            "Hello, world!",
            id="single multiline block - to be formatted",
        ),
        pytest.param(
            (
                """
                Hello, world!
                Goodbye, world!
                """,
                "",
                None,
                """
                    Oh hey there, world!
                    Wait - is that a meteor?
                """,
                "",
            ),
            "Hello, world!\nGoodbye, world!\n\nOh hey there, world!\nWait - is that a meteor?",
            id="multiple blocks - to be formatted",
        ),
    ),
)
def test_promptify(
    blocks: tuple[str | None, ...],
    expected: str,
) -> None:
    """Test compose_text with no blocks."""
    assert promptify(*blocks) == expected


def test_promptify_custom_joiner() -> None:
    """Test compose_text with a custom joiner."""
    block1 = """
        Hello, world!
        """
    block2 = """
        Goodbye, world!
        """
    expected = "Hello, world!\n---\nGoodbye, world!"
    assert promptify(block1, block2, joiner="\n---\n") == expected
