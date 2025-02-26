"""Defines a data structure for representing a repository."""

from typing import Self

from pydantic import BaseModel


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
    def from_repo_full_name(cls, repo_full_name: str) -> Self:
        """Creates a RepoReference object from a full repository name string.

        Args:
            repo_full_name: The full name of the repository in the format 'owner/name'.

        Returns:
            A RepoReference object.

        Raises:
            ValueError: If the repository full name is not in the correct format.
        """
        owner, name = repo_full_name.split("/")
        return cls(owner=owner, name=name)
