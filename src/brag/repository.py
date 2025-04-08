"""Defines a data structure for representing a repository."""

import re
from typing import Annotated, Self

from pydantic import BaseModel, StringConstraints

REPO_FULL_NAME_PATTERN = r"^(?P<owner>[a-zA-Z0-9_-]+)\/(?P<name>[a-zA-Z0-9_-]+)$"
type RepoFullName = Annotated[str, StringConstraints(pattern=REPO_FULL_NAME_PATTERN)]

REPO_URL_PATTERN = r"^https?://github\.com/(?P<owner>[a-zA-Z0-9_-]+)/(?P<name>[a-zA-Z0-9_-]+)(?:\.git)?$"
type GitHubRepoURL = Annotated[str, StringConstraints(pattern=REPO_URL_PATTERN)]


class InvalidRepoFullName(ValueError):
    """Raised when a repository full name is invalid."""

    def __init__(self, repo_full_name: str):
        self.repo_full_name = repo_full_name
        self.expected_format = REPO_FULL_NAME_PATTERN
        self.message = f"Invalid repository full name: {repo_full_name!r}. Must match the pattern: {self.expected_format!r}"
        super().__init__(self.message)


class InvalidGitHubRepoURL(ValueError):
    """Raised when a GitHub repository URL is invalid."""

    def __init__(self, github_repo_url: str):
        self.github_repo_url = github_repo_url
        self.expected_format = REPO_URL_PATTERN
        self.message = f"Invalid GitHub repository URL: {github_repo_url!r}. Must match the pattern: {self.expected_format!r}"
        super().__init__(self.message)


class RepoReference(BaseModel):
    """A reference to a repository on a code hosting platform.

    Attributes:
        owner: The owner of the repository (e.g., a user or organization).
        name: The name of the repository.
    """

    owner: str
    name: str

    @property
    def full_name(self) -> str:
        """Returns the full name of the repository in the format 'owner/name'."""
        return f"{self.owner}/{self.name}"

    @classmethod
    def from_repo_full_name(cls, repo_full_name: RepoFullName) -> Self:
        """Create a RepoReference object from a RepoFullName object.

        Args:
            repo_full_name: A repository full name in the format 'owner/name'.

        Returns:
            A RepoReference object.
        """
        m = re.match(REPO_FULL_NAME_PATTERN, repo_full_name)
        if not m:
            raise InvalidRepoFullName(repo_full_name)
        owner = m.group("owner")
        name = m.group("name")
        return cls(owner=owner, name=name)

    @classmethod
    def from_github_repo_url(cls, github_repo_url: GitHubRepoURL) -> Self:
        """Create a RepoReference object from a GitHub repository URL.

        Args:
            github_repo_url: A GitHub repository URL in the format 'https://github.com/owner/name'.
                The URL can be HTTP or HTTPS.
                The URL can end with or without a trailing '.git' suffix.

        Returns:
            A RepoReference object.
        """
        m = re.match(REPO_URL_PATTERN, github_repo_url)
        if not m:
            raise InvalidGitHubRepoURL(github_repo_url)
        owner = m.group("owner")
        name = m.group("name")
        return cls(owner=owner, name=name)
