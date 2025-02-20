from collections.abc import Iterator
from datetime import datetime
from itertools import islice

from github import Github
from github.Commit import Commit
from github.File import File
from github.GithubObject import NotSet
from langchain_core.document_loaders import BaseLoader
from langchain_core.documents import Document
from pydantic import BaseModel, ConfigDict


class GithubCommitLoader(BaseLoader, BaseModel):
    """Loader for Github commits."""

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )

    github: Github
    user: str
    repo_owner: str
    repo_name: str
    from_date: datetime | None = None
    to_date: datetime | None = None
    limit: int | None = None

    def lazy_load(self) -> Iterator[Document]:
        """Lazy load the commits from the Github API."""
        commits = islice(self._iter_commits(), self.limit)
        return map(_github_commit_to_document, commits)

    def _iter_commits(self) -> Iterator[Commit]:
        """Iterate over the commits from the Github API."""
        repo = self.github.get_repo(f"{self.repo_owner}/{self.repo_name}")
        commits = repo.get_commits(
            author=self.user,
            since=self.from_date or NotSet,
            until=self.to_date or NotSet,
        )
        yield from commits


def _github_commit_to_document(commit: Commit) -> Document:
    """Convert a Github commit to a LangChain document."""
    return Document(
        page_content=_format_commit_diff_and_message(commit),
        metadata={
            "url": commit.html_url,
            "date": commit.commit.author.date,
            "author": commit.author.login,
            "title": commit.commit.message.splitlines()[0].strip(),
        },
    )


def _format_commit_diff_and_message(commit: Commit) -> str:
    """Format the commit diff and message into a single string."""
    return "\n\n".join(
        (
            commit.commit.message.strip(),
            *map(_format_commit_file, commit.files),
        )
    )


def _format_commit_file(file: File) -> str:
    """Format the commit file into a string."""
    file_header = f"{file.status.upper()} {file.filename}:"

    if file.patch is not None:
        return "\n".join((file_header, file.patch))
    else:
        return f"{file_header} (cannot show diff)"
