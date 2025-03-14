"""Sources of data."""

from __future__ import annotations

import abc
from collections.abc import Callable, Iterator
from dataclasses import dataclass
from itertools import islice


class DataSource[T](abc.ABC):
    """A source of data."""

    @abc.abstractmethod
    def __iter__(self) -> Iterator[T]: ...

    @abc.abstractmethod
    def __len__(self) -> int: ...

    def limit(self, count: int) -> LimitDataSource[T]:
        """Limit the number of items this data source yields."""
        return LimitDataSource(self, count)

    def map[R](self, mapper: Callable[[T], R]) -> MapDataSource[T, R]:
        """Map a function over a data source."""
        return MapDataSource(self, mapper)


@dataclass(frozen=True, slots=True)
class LimitDataSource[T](DataSource[T]):
    """A data source that limits the number of items it yields."""

    inner: DataSource[T]
    count: int

    def __iter__(self) -> Iterator[T]:
        return islice(self.inner, self.count)

    def __len__(self) -> int:
        return min(self.count, len(self.inner))


@dataclass(frozen=True, slots=True)
class MapDataSource[T, R](DataSource[R]):
    """A data source that maps a function over a data source."""

    inner: DataSource[T]
    mapper: Callable[[T], R]

    def __iter__(self) -> Iterator[R]:
        return map(self.mapper, self.inner)

    def __len__(self) -> int:
        return len(self.inner)
