"""Fetch and format Github commits.

This module provides functionality to:
- Fetch commits from a Github repository for a specific user.
- Format commit information into a context string suitable for generating brag documents.
"""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass
from datetime import datetime
from itertools import islice

from github import Github
from github.Commit import Commit
from github.File import File
from github.GithubObject import NotSet
from github.PaginatedList import PaginatedList

from brag.repository import RepoReference


@dataclass(frozen=True, slots=True)
class GithubCommits:
    """A class to fetch Github commits from a repository for a specific user.

    Attributes:
        _commits: A paginated list of Commit objects.
        repo: A RepoReference object representing the repository.
        user: The username of the author whose commits are being fetched.
        limit: The maximum number of commits to fetch. If None, all commits are fetched.

    """

    _commits: PaginatedList[Commit]
    repo: RepoReference
    user: str
    limit: int | None = None

    @classmethod
    def from_github(
        cls,
        github: Github,
        repo: RepoReference,
        user: str,
        from_date: datetime | None = None,
        to_date: datetime | None = None,
        limit: int | None = None,
    ) -> GithubCommits:
        """Create a GithubCommits instance from the Github API.

        Args:
            github: A Github API client instance.
            repo: A RepoReference object representing the repository.
            user: The username of the author whose commits are being fetched.
            from_date: An optional datetime object representing the start date for fetching commits.
            to_date: An optional datetime object representing the end date for fetching commits.
            limit: An optional integer representing the maximum number of commits to fetch.

        Returns:
            A GithubCommits instance.

        """
        github_repo = github.get_repo(repo.full_name)
        commits = github_repo.get_commits(
            author=user,
            since=from_date or NotSet,
            until=to_date or NotSet,
        )
        return cls(
            commits,
            repo=repo,
            user=user,
            limit=limit,
        )

    def __iter__(self) -> Iterator[Commit]:
        return islice(self._commits, self.limit)

    def __len__(self) -> int:
        if self.limit is not None:
            return min(self.total_count, self.limit)
        else:
            return self.total_count

    @property
    def total_count(self) -> int:
        """Return the total count of commits.

        This is similar to `len(self)`, except that this property ignores the `limit` parameter.
        """
        return self._commits.totalCount


def format_commit_as_context(commit: Commit) -> str:
    """Format a Github commit as a context string.

    This function takes a Github commit object and formats it into a string
    that includes the commit message and the diffs of the files changed in the commit.

    Args:
        commit: The Github commit object to format.

    Returns:
        A string containing the commit message and file diffs.

    """
    return "\n\n".join(
        (
            commit.commit.message.strip(),
            *map(_format_commit_file, commit.files),
        )
    )


def _format_commit_file(file: File) -> str:
    """Format the commit file into a context string."""
    file_header = f"{file.status.upper()} {file.filename}:"

    if file.patch is not None:
        return "\n".join((file_header, file.patch))
    else:
        return f"{file_header} (cannot show diff)"
