"""Load and format Git commits from a local repository.

This module provides functionality to:
- Load commits from a local Git repository.
- Format commit information into a context string suitable for generating brag documents.
"""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass
from datetime import datetime
from functools import cached_property
from pathlib import Path
from typing import Any

from git import Repo

from brag.sources import DataSource

type GitCommit = str


@dataclass(frozen=True, slots=True)
class GitCommitsSource(DataSource[GitCommit]):
    """A class to load Git commits from a local repository.

    Attributes:
        path: A Path object representing the local repository.
        author: The username of the author whose commits are being fetched.
        from_date: An optional datetime object representing the start date for fetching commits.
        to_date: An optional datetime object representing the end date for fetching commits.
    """

    path: Path
    author: str
    from_date: datetime | None = None
    to_date: datetime | None = None

    def __iter__(self) -> Iterator[GitCommit]:
        return iter(self._commits)

    def __len__(self) -> int:
        return len(self._commits)

    @cached_property
    def _commits(self) -> tuple[GitCommit, ...]:
        repo = Repo(self.path)

        # Build kwargs for filtering commits
        kwargs: dict[str, Any] = {"author": self.author}

        # Add date filters if specified
        if self.from_date is not None:
            kwargs["since"] = self.from_date
        if self.to_date is not None:
            kwargs["until"] = self.to_date

        # Get commits for the specified author
        commits_iter = repo.iter_commits(**kwargs)

        # Convert iterator to tuple to ensure it doesn't get exhausted
        # This is more memory-intensive but prevents issues with iteration
        return tuple(repo.git.show(commit) for commit in commits_iter)
