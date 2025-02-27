"""Utilities for working with asyncio, including a decorator to run an async function synchronously."""

import asyncio
import functools
from collections.abc import Callable, Coroutine
from typing import Any, ParamSpec, TypeVar

_P = ParamSpec("_P")
_R = TypeVar("_R")


def run_with_asyncio(
    f: Callable[_P, Coroutine[Any, Any, _R]],
) -> Callable[_P, _R]:
    """Run an async function synchronously.

    This decorator takes an async function and returns a synchronous
    function that runs the async function in an asyncio event loop.

    Args:
        f: The async function to run synchronously.

    Returns:
        A synchronous function that runs the async function.

    """

    @functools.wraps(f)
    def wrapper(*args: _P.args, **kwargs: _P.kwargs) -> _R:
        return asyncio.run(f(*args, **kwargs))

    return wrapper
