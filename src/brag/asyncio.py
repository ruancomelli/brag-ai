import asyncio
import functools
from collections.abc import Awaitable, Callable
from typing import ParamSpec, TypeVar

_P = ParamSpec("_P")
_R = TypeVar("_R")


def run_with_asyncio(
    f: Callable[_P, Awaitable[_R]],
) -> Callable[_P, _R]:
    @functools.wraps(f)
    def wrapper(*args: _P.args, **kwargs: _P.kwargs) -> _R:
        return asyncio.run(f(*args, **kwargs))

    return wrapper
