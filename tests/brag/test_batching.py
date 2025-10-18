"""Tests for the batching module."""

import pytest

from brag.batching import batch_chunks_by_token_limit


@pytest.mark.parametrize(
    ("chunks", "max_tokens", "expected_batches"),
    (
        pytest.param(
            [],
            100,
            [],
            id="empty chunks",
        ),
        pytest.param(
            ["single chunk"],
            100,
            ["single chunk"],
            id="single chunk",
        ),
        pytest.param(
            ["chunk1", "chunk2", "chunk3"],
            100,
            ["chunk1\n\n---\n\nchunk2\n\n---\n\nchunk3"],
            id="multiple chunks within limit",
        ),
        pytest.param(
            ["very long chunk that exceeds the token limit by a lot"],
            1,
            ["very long chunk that exceeds the token limit by a lot"],
            id="single chunk exceeding limit",
        ),
        pytest.param(
            ["chunk1", "chunk2", "chunk3"],
            1,
            ["chunk1", "chunk2", "chunk3"],
            id="all chunks exceeding limit",
        ),
        pytest.param(
            ["chunk1", "chunk2", "chunk3", "chunk4", "chunk5"],
            10,
            ["chunk1\n\n---\n\nchunk2", "chunk3\n\n---\n\nchunk4", "chunk5"],
            id="group only some chunks",
        ),
        pytest.param(
            ["chunk1", "", "chunk3", "", "chunk5"],
            10,
            ["chunk1", "chunk3\n\n---\n\nchunk5"],
            id="some empty chunks",
        ),
    ),
)
def test_batch_chunks_by_token_limit_basic_cases(
    chunks: list[str],
    max_tokens: int,
    expected_batches: list[str],
) -> None:
    """Test basic batching scenarios."""
    result = list(batch_chunks_by_token_limit(chunks, max_tokens))
    assert result == expected_batches


@pytest.mark.parametrize(
    ("chunks", "max_tokens", "joiner", "expected_batches"),
    (
        pytest.param(
            ["chunk1", "chunk2", "chunk3", "chunk4", "chunk5"],
            8,
            "|",
            ["chunk1|chunk2", "chunk3|chunk4|chunk5"],
            id="small joiner",
        ),
        pytest.param(
            ["chunk1", "chunk2", "chunk3", "chunk4", "chunk5"],
            8,
            " <<JOINER>> ",
            ["chunk1", "chunk2 <<JOINER>> chunk3", "chunk4 <<JOINER>> chunk5"],
            id="large joiner",
        ),
        pytest.param(
            ["chunk1", "chunk2", "chunk3", "chunk4", "chunk5"],
            8,
            "",
            ["chunk1chunk2chunk3chunk4", "chunk5"],
            id="empty joiner",
        ),
    ),
)
def test_batch_chunks_by_token_limit_different_joiners(
    chunks: list[str],
    max_tokens: int,
    joiner: str,
    expected_batches: list[str],
) -> None:
    """Test batching with different joiners."""
    result = list(batch_chunks_by_token_limit(chunks, max_tokens, joiner=joiner))
    assert result == expected_batches
