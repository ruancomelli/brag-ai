"""Batch text chunks together to fit within a max tokens per batch.

The max tokens per batch is expected to be a subset of the model's context window size.
"""

from collections.abc import Iterable, Iterator

from brag.models import TokenCount
from brag.text_formatters import promptify
from brag.tokens import estimate_token_count


def batch_chunks_by_token_limit(
    chunks: Iterable[str],
    max_tokens_per_batch: TokenCount,
    joiner: str = "\n\n---\n\n",
) -> Iterator[str]:
    """Batch text chunks together to fit within a max tokens per batch.

    This function takes an iterable of text chunks and combines them into larger
    batches that will fit within the specified max tokens per batch. It uses
    token estimation to determine how many chunks can be combined safely.

    Chunks are combined with a joiner (defined by the `joiner` parameter) to help
    the model distinguish between different chunks in the same batch. The joiner is
    surrounded by double newlines for better visual separation.

    This batching optimizes API usage by reducing the number of calls to the LLM provider,
    which can help avoid rate limiting errors for repositories with many commits or
    other text chunks.

    The size of each chunk is overestimated to be conservative, that is, to ensure that the chunk
    will fit within the max tokens per batch. The size of each batch is estimated by summing the
    sizes of its chunks, which is also an approximation.

    Args:
        chunks: An iterable of strings, where each string is a chunk of text.
        max_tokens_per_batch: The maximum number of tokens allowed per batch.
        joiner: The string to use for joining chunks when batching them together.

    Yields:
        Batches of text chunks, each fitting within the max tokens per batch.
    """
    joiner_token_count = estimate_token_count(joiner, approximation_mode="overestimate")
    current_batch: str = ""
    current_batch_token_count = 0

    for chunk in chunks:
        # Use the overestimate strategy to be conservative, that is, to ensure that the chunk
        # will fit within the max tokens per batch.
        chunk_token_count = estimate_token_count(
            chunk, approximation_mode="overestimate"
        )

        # If adding this chunk would exceed the limit, yield the current batch and start a new one
        if current_batch and (
            current_batch_token_count + joiner_token_count + chunk_token_count
            > max_tokens_per_batch
        ):
            yield current_batch
            current_batch = chunk
            current_batch_token_count = chunk_token_count
        else:
            current_batch = promptify(current_batch, chunk, joiner=joiner)
            current_batch_token_count += joiner_token_count + chunk_token_count

    # Add the last batch if it's not empty
    if current_batch:
        yield current_batch
