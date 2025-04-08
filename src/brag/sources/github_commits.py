"""Fetch and format Github commits.

This module provides functionality to:
- Fetch commits from a Github repository for a specific user.
- Format commit information into a context string suitable for generating brag documents.
"""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass
from datetime import datetime
from functools import cached_property

from github import Github
from github.Commit import Commit as GithubCommit
from github.File import File
from github.GithubObject import NotSet
from github.PaginatedList import PaginatedList

from brag.repository import RepoReference
from brag.sources import DataSource

type FormattedGithubCommit = str


@dataclass(frozen=True, slots=True)
class GithubCommitsSource(DataSource[FormattedGithubCommit]):
    """A class to fetch Github commits from a repository for a specific user.

    Attributes:
        github: A Github API client instance.
        repo: A RepoReference object representing the repository.
        author: The username of the author whose commits are being fetched.
        from_date: An optional datetime object representing the start date for fetching commits.
        to_date: An optional datetime object representing the end date for fetching commits.
    """

    github: Github
    repo: RepoReference
    author: str
    from_date: datetime | None = None
    to_date: datetime | None = None

    def __iter__(self) -> Iterator[FormattedGithubCommit]:
        return map(_format_github_commit_as_prompt_context, self._commits)

    def __len__(self) -> int:
        return self._commits.totalCount

    @cached_property
    def _commits(self) -> PaginatedList[GithubCommit]:
        return self.github.get_repo(self.repo.full_name).get_commits(
            author=self.author,
            since=self.from_date or NotSet,
            until=self.to_date or NotSet,
        )


def _format_github_commit_as_prompt_context(
    commit: GithubCommit,
) -> FormattedGithubCommit:
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
    return f"{file.status.upper()} {file.filename}:\n{file.patch}"
