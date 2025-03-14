"""Defines a data structure for representing a repository."""

from typing import Annotated, Self

from pydantic import BaseModel, StringConstraints

type RepoFullName = Annotated[
    str,
    StringConstraints(pattern=r"^[a-zA-Z0-9_-]+\/[a-zA-Z0-9_-]+$"),
]

type GitHubRepoURL = Annotated[
    str,
    StringConstraints(
        pattern=r"^https?://github\.com/[a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+(?:\.git)?$"
    ),
]


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
            repo_full_name: A RepoFullName object.

        Returns:
            A RepoReference object.
        """
        owner, name = repo_full_name.split("/")
        return cls(owner=owner, name=name)

    @classmethod
    def from_github_repo_url(cls, github_repo_url: GitHubRepoURL) -> Self:
        """Create a RepoReference object from a GitHub repository URL.

        Args:
            github_repo_url: A GitHub repository URL.

        Returns:
            A RepoReference object.
        """
        repo_full_name = (
            github_repo_url.removesuffix(".git")
            .removeprefix("https://github.com/")
            .removeprefix("http://github.com/")
        )
        return cls.from_repo_full_name(repo_full_name)
