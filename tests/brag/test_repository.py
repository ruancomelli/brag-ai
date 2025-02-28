"""Tests for the repository module."""

import pytest

from brag.repository import RepoReference


def test_repo_reference_creation() -> None:
    """Test that a RepoReference object can be created."""
    repo_reference = RepoReference(owner="test_owner", name="test_repo")
    assert repo_reference.owner == "test_owner"
    assert repo_reference.name == "test_repo"


def test_repo_reference_full_name() -> None:
    """Test the `full_name` property."""
    repo_reference = RepoReference(owner="test_owner", name="test_repo")
    assert repo_reference.full_name == "test_owner/test_repo"


@pytest.mark.parametrize(
    "repo_full_name, expected_owner, expected_name",
    [
        ("owner1/repo1", "owner1", "repo1"),
        ("owner2/repo2", "owner2", "repo2"),
    ],
)
def test_from_repo_full_name(
    repo_full_name: str,
    expected_owner: str,
    expected_name: str,
) -> None:
    """Test creating a RepoReference from a full name."""
    repo = RepoReference.from_repo_full_name(repo_full_name)
    assert repo.owner == expected_owner
    assert repo.name == expected_name
    assert repo.full_name == repo_full_name


def test_from_repo_full_name_raises_value_error() -> None:
    """Test that from_repo_full_name raises a ValueError for invalid input."""
    with pytest.raises(ValueError):
        RepoReference.from_repo_full_name("invalid-repo-name")
