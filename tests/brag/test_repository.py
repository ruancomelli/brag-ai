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
    ("repo_full_name", "expected_owner", "expected_name"),
    (
        ("owner1/repo1", "owner1", "repo1"),
        ("owner2/repo2", "owner2", "repo2"),
    ),
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


@pytest.mark.parametrize(
    ("github_repo_url", "expected_owner", "expected_name"),
    (
        ("https://github.com/owner1/repo1", "owner1", "repo1"),
        ("http://github.com/owner2/repo2", "owner2", "repo2"),
        ("https://github.com/owner3/repo3.git", "owner3", "repo3"),
    ),
)
def test_from_github_repo_url(
    github_repo_url: str,
    expected_owner: str,
    expected_name: str,
) -> None:
    """Test creating a RepoReference from a GitHub repository URL."""
    repo = RepoReference.from_github_repo_url(github_repo_url)
    assert repo.owner == expected_owner
    assert repo.name == expected_name
    assert repo.full_name == f"{expected_owner}/{expected_name}"


@pytest.mark.parametrize(
    "invalid_url",
    (
        "https://gitlab.com/owner/repo",
        "github.com/owner/repo",
        "https://github.com/owner",
    ),
)
def test_from_github_repo_url_raises_value_error(invalid_url: str) -> None:
    """Test that from_github_repo_url raises a ValueError for invalid input."""
    with pytest.raises(ValueError):
        RepoReference.from_github_repo_url(invalid_url)
