"""Defines a data structure for representing a repository."""

from typing import Annotated, Self

from pydantic import BaseModel, StringConstraints

type RepoFullName = Annotated[
    str,
    StringConstraints(pattern=r"^[a-zA-Z0-9_-]+\/[a-zA-Z0-9_-]+$"),
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
