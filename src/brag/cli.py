from __future__ import annotations

import enum
import sys
from datetime import datetime
from pathlib import Path
from typing import Annotated, Self

from github import Github
from github.Auth import Token
from loguru import logger
from pydantic import BaseModel
from rich.console import Console
from typer import Argument, BadParameter, Option, Typer

from brag.github_commit_loader import GithubCommitLoader

app = Typer(
    rich_markup_mode="rich",
    help=(
        "Generate and maintain a brag document automatically from your GitHub contributions,"
        " powered by AI."
    ),
    no_args_is_help=True,
)


class RepoArgument(BaseModel):
    owner: str
    name: str

    @property
    def full_name(self) -> str:
        return f"{self.owner}/{self.name}"

    @classmethod
    def parse(cls, value: str) -> Self:
        owner, name = value.split("/")
        return cls(owner=owner, name=name)


class OutputFormat(enum.StrEnum):
    MARKDOWN = enum.auto()

    @classmethod
    def default(cls) -> OutputFormat:
        return OutputFormat.MARKDOWN


@app.command()
def from_repo(
    repo: Annotated[
        RepoArgument,
        Argument(
            help="The repository to generate the brag document for. Format: `owner/repo`",
            rich_help_panel="Inputs",
            parser=RepoArgument.parse,
        ),
    ],
    user_login: Annotated[
        str | None,
        Option(
            "-u",
            "--user",
            help=(
                "The user to generate the brag document for."
                " If not provided, the owner of the GitHub API token will be used."
            ),
            rich_help_panel="Inputs",
        ),
    ] = None,
    from_date: Annotated[
        datetime | None,
        Option(
            help="The start date to generate the brag document for",
            rich_help_panel="Inputs",
        ),
    ] = None,
    to_date: Annotated[
        datetime | None,
        Option(
            help="The end date to generate the brag document for",
            rich_help_panel="Inputs",
        ),
    ] = None,
    limit: Annotated[
        int | None,
        Option(
            help="The maximum number of commits to include in the brag document",
            rich_help_panel="Inputs",
        ),
    ] = None,
    token: Annotated[
        str | None,
        Option(
            help=(
                "The GitHub token to use to fetch information from GitHub."
                " If not provided, the brag document will only include public information."
            ),
            envvar="GITHUB_API_TOKEN",
            rich_help_panel="Inputs",
        ),
    ] = None,
    format: Annotated[
        OutputFormat,
        Option(
            help="The format to generate the brag document in",
            rich_help_panel="Outputs",
        ),
    ] = OutputFormat.default(),
    output: Annotated[
        Path | None,
        Option(
            "-o",
            "--output",
            help="Path to save the commit history. Outputs Markdown-formatted text to stdout if not specified.",
            rich_help_panel="Outputs",
        ),
    ] = None,
    overwrite: Annotated[
        bool,
        Option(
            "--overwrite",
            help="If set, overwrites the output file if it already exists.",
            rich_help_panel="Outputs",
        ),
    ] = False,
) -> None:
    if output is not None and output.exists() and not overwrite:
        raise FileExistsError(
            f"Output file `{output}` already exists. Use `--overwrite` to overwrite."
        )

    if not user_login and not token:
        raise BadParameter("Either `user` or `github_api_token` must be provided")

    with Github(auth=Token(token) if token else None) as g:
        if not user_login:
            user_login = g.get_user().login

        loader = GithubCommitLoader(
            github=g,
            user=user_login,
            repo_owner=repo.owner,
            repo_name=repo.name,
            from_date=from_date,
            to_date=to_date,
            limit=limit,
        )

        documents = loader.load()

        # Open the output file if specified, otherwise use stdout
        with open(output, "w") if output else sys.stdout as f:
            console = Console(file=f)

            logger.info(
                "Generating brag document for {user_login} from {from_date} to {to_date} in {format} format",
                user_login=user_login,
                from_date=from_date,
                to_date=to_date,
                format=format,
            )

            console.print(documents)
