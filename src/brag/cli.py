"""Command-line interface for the brag application.

This script uses Typer to create a CLI that allows users to generate brag documents
from their GitHub contributions.
"""

from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path
from typing import Annotated
from typing import get_args as get_literal_type_args

import click
from github import Github
from github.Auth import Token
from loguru import logger
from pydantic_ai.models import KnownModelName
from typer import Argument, BadParameter, Option, Typer

from brag.agents import generate_brag_document
from brag.asyncio import run_with_asyncio
from brag.github_commits import GithubCommits, format_commit_as_context
from brag.repository import RepoReference

app = Typer(
    rich_markup_mode="rich",
    help=(
        "Generate and maintain a brag document automatically from your GitHub contributions,"
        " powered by AI."
    ),
    no_args_is_help=True,
)


@app.command()
@run_with_asyncio
async def from_repo(
    repo: Annotated[
        RepoReference,
        Argument(
            help="The repository to generate the brag document for. Format: `owner/repo`",
            rich_help_panel="Inputs",
            parser=RepoReference.from_repo_full_name,
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
            "--from",
            help="The start date to generate the brag document for",
            rich_help_panel="Inputs",
        ),
    ] = None,
    to_date: Annotated[
        datetime | None,
        Option(
            "--to",
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
    github_api_token: Annotated[
        str | None,
        Option(
            "--token",
            help=(
                "The GitHub token to use to fetch information from GitHub."
                " If not provided, the brag document will only include public information."
            ),
            envvar="GITHUB_API_TOKEN",
            rich_help_panel="Inputs",
        ),
    ] = None,
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
    model_name: Annotated[
        KnownModelName,
        Option(
            "--model",
            help="The name of the model to use for generating the brag document.",
            rich_help_panel="Model",
            # Workaround since `typer` does not currently support `Literal` types
            # See https://github.com/fastapi/typer/pull/429#issuecomment-2491043848
            click_type=click.Choice(get_literal_type_args(KnownModelName)),
        ),
    ] = (
        # TODO: experiment with other models to pick the best default
        "google-vertex:gemini-2.0-flash"
    ),
    language: Annotated[
        str,
        Option(
            "--language",
            help="The language to use for generating the brag document.",
            rich_help_panel="Model",
        ),
    ] = "english",
) -> None:
    """Generate a brag document from a GitHub repository.

    This command fetches commits from a specified GitHub repository for a given user,
    and then uses an AI model to generate a brag document summarizing those contributions.
    """
    if output is not None and output.exists() and not overwrite:
        raise FileExistsError(
            f"Output file `{output}` already exists. Use `--overwrite` to overwrite."
        )

    if not user_login and not github_api_token:
        raise BadParameter("Either `user` or `github_api_token` must be provided")

    logger.info(
        (
            "Generating brag document from {repo_full_name} for {user_login}"
            "{from_date}{to_date}"
        ),
        repo_full_name=repo.full_name,
        user_login=user_login,
        from_date=f" from {from_date}" if from_date else "",
        to_date=f" to {to_date}" if to_date else "",
    )

    with Github(auth=Token(github_api_token) if github_api_token else None) as g:
        if not user_login:
            user_login = g.get_user().login

        commits = GithubCommits.from_github(
            github=g,
            user=user_login,
            repo=repo,
            from_date=from_date,
            to_date=to_date,
            limit=limit,
        )

        context_chunks = map(format_commit_as_context, commits)

        brag_document = await generate_brag_document(
            model_name,
            context_chunks,
            language=language,
        )

    # Open the output file if specified, otherwise use stdout
    with open(output, "w") if output else sys.stdout as f:
        f.write(brag_document)
