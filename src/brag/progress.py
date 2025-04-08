"""Helper functions for tracking the progress of long-running operations."""

from collections.abc import Iterable, Iterator
from functools import cache

from rich.progress import BarColumn, MofNCompleteColumn, Progress, SpinnerColumn


def track_iterable_progress[T](
    iterable: Iterable[T],
    /,
    *,
    description: str,
) -> Iterator[T]:
    """Track the progress of an iterable.

    This function is a helper that creates a progress bar and tracks the progress of
    an iterable. It's useful for tracking the progress of a long-running operation,
    such as generating the brag document.
    """
    with _progress_bar(description=description) as progress:
        yield from progress.track(iterable)


def _progress_bar(*, description: str) -> Progress:
    """Create a progress bar with a description.

    This function is a helper that creates a progress bar with a description.
    Useful for ensuring a consistent progress bar across the CLI.
    """
    return Progress(
        _get_spinner_column(),
        f"[progress.description]{description}",
        _get_mofncomplete_column(),
        _get_bar_column(),
        "[progress.percentage]({task.percentage:>3.0f}%)",
        "[progress.elapsed](Elapsed: {task.elapsed:.2f}s)",
    )


@cache
def _get_spinner_column():
    return SpinnerColumn(spinner_name="point")


@cache
def _get_mofncomplete_column():
    return MofNCompleteColumn()


@cache
def _get_bar_column():
    return BarColumn()
