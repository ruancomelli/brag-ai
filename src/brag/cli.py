"""Command-line interface for the brag application.

This script uses Typer to create a CLI that allows users to generate brag documents
from their GitHub contributions.
"""

import json
import sys
from datetime import datetime
from itertools import groupby
from pathlib import Path
from typing import Annotated, Literal

import cyclopts
from github import Github
from github.Auth import Token
from loguru import logger
from rich.console import Console
from rich.progress import MofNCompleteColumn, Progress, SpinnerColumn

from brag import __version__
from brag.agents import generate_brag_document
from brag.batching import batch_chunks_by_token_limit
from brag.models import (
    AVAILABLE_MODEL_FULL_NAMES,
    AVAILABLE_MODELS,
    AvailableModelFullName,
    Model,
)
from brag.repository import GitHubRepoURL, RepoFullName, RepoReference
from brag.sources import DataSource
from brag.sources.git_commits import GitCommit, GitCommitsSource
from brag.sources.github_commits import FormattedGithubCommit, GithubCommitsSource

COMMIT_BATCH_JOINER = "\n\n---\n\n"

app = cyclopts.App(
    console=Console(),
    help=(
        "Generate and maintain a brag document automatically from your GitHub contributions,"
        " powered by AI."
    ),
    help_format="md",
    version=__version__,
    version_flags=("--version", "-V"),
    config=cyclopts.config.Env(prefix="BRAG_", command=False),
    # TODO: check how to migrate the following options to `cyclopts`
    # rich_markup_mode="rich",
    # no_args_is_help=True,
)

inputs_group = cyclopts.Group("Inputs")
outputs_group = cyclopts.Group("Outputs")
model_group = cyclopts.Group("Model")


@app.command
async def from_repo(
    repo_full_name: Annotated[
        RepoFullName | GitHubRepoURL,
        cyclopts.Parameter(
            name="--repo",
            help="The repository to generate the brag document for. Format: `owner/repo` or a GitHub URL",
            group=inputs_group,
        ),
    ],
    author: Annotated[
        str | None,
        cyclopts.Parameter(
            name=("-u", "--user"),
            help=(
                "The user to generate the brag document for."
                " If not provided, the owner of the GitHub API token will be used."
            ),
            group=inputs_group,
        ),
    ] = None,
    from_date: Annotated[
        datetime | None,
        cyclopts.Parameter(
            name="--from",
            help="The start date to generate the brag document for",
            group=inputs_group,
        ),
    ] = None,
    to_date: Annotated[
        datetime | None,
        cyclopts.Parameter(
            name="--to",
            help="The end date to generate the brag document for",
            group=inputs_group,
        ),
    ] = None,
    limit: Annotated[
        int | None,
        cyclopts.Parameter(
            help="The maximum number of commits to include in the brag document",
            group=inputs_group,
        ),
    ] = None,
    github_api_token: Annotated[
        str | None,
        cyclopts.Parameter(
            help=(
                "The GitHub token to use to fetch information from GitHub."
                " If not provided, the brag document will only include public information."
            ),
            group=inputs_group,
        ),
    ] = None,
    output: Annotated[
        Path | None,
        cyclopts.Parameter(
            name=("-o", "--output"),
            help="Path to save the commit history. Outputs Markdown-formatted text to stdout if not specified.",
            group=outputs_group,
        ),
    ] = None,
    overwrite: Annotated[
        bool,
        cyclopts.Parameter(
            name="--overwrite",
            help="If set, overwrites the output file if it already exists.",
            group=outputs_group,
        ),
    ] = False,
    model_name: Annotated[
        AvailableModelFullName,
        cyclopts.Parameter(
            name="--model",
            help=(
                "The name of the model to use for generating the brag document."
                " See `brag list-models` for the list of available models."
            ),
            group=model_group,
            show_choices=False,
        ),
    ] = "google-gla:gemini-2.0-flash",
    language: Annotated[
        str,
        cyclopts.Parameter(
            "--language",
            help="The language to use for generating the brag document.",
            group=model_group,
        ),
    ] = "english",
    buffer_percentage: Annotated[
        float,
        cyclopts.Parameter(
            help=(
                "The percentage of the model's context window to reserve as a buffer when batching commits."
                " Higher values (e.g., 0.3) are more conservative, while lower values (e.g., 0.1) allow for more chunks per batch but increase the risk of accidentally exceeding the limit."
            ),
            group=model_group,
        ),
    ] = 0.2,
) -> None:
    """Generate a brag document from a GitHub repository.

    This command fetches commits from a specified GitHub repository for a given user,
    and then uses an AI model to generate a brag document summarizing those contributions.

    To optimize performance and avoid rate limiting issues, commits are batched together
    into larger chunks that fit within the model's context window. This significantly
    reduces the number of API calls to the LLM provider for repositories with many commits.

    The batching process uses token count estimation to determine how many commits
    can be combined safely. The `--buffer-percentage` parameter allows you to control
    how conservative this batching should be by reserving a portion of the model's
    context window as a safety buffer.
    """
    if output is not None and output.exists() and not overwrite:
        raise FileExistsError(
            f"Output file `{output}` already exists. Use `--overwrite` to overwrite."
        )

    if not author and not github_api_token:
        raise ValueError("Either `user` or `github_api_token` must be provided")

    if model_name not in AVAILABLE_MODEL_FULL_NAMES:
        raise ValueError(
            f"Model `{model_name}` is not available. See `brag list-models` for the list of available models."
        )

    model = Model.from_full_name(model_name)

    logger.info(
        ("Generating brag document from {repo} for {author}{from_date}{to_date}"),
        repo=repo_full_name,
        author=author,
        from_date=f" from {from_date}" if from_date else "",
        to_date=f" to {to_date}" if to_date else "",
    )

    # Parse the repo reference based on the input format
    if repo_full_name.startswith(("http://", "https://")):
        repo = RepoReference.from_github_repo_url(repo_full_name)
    else:
        repo = RepoReference.from_repo_full_name(repo_full_name)

    with Github(auth=Token(github_api_token) if github_api_token else None) as g:
        if not author:
            author = g.get_user().login

        github_commits: DataSource[FormattedGithubCommit] = GithubCommitsSource(
            github=g,
            author=author,
            repo=repo,
            from_date=from_date,
            to_date=to_date,
        )
        if limit:
            github_commits = github_commits.limit(limit)

        commits_count = len(github_commits)

        logger.info(
            "Processing {commits} for {author} in {repo}",
            commits=(
                f"{commits_count} commits"
                if commits_count > 1
                else f"{commits_count} commit"
            ),
            author=author,
            repo=repo.full_name,
        )

        # Batch chunks to respect rate limits
        batched_chunks = tuple(
            batch_chunks_by_token_limit(
                github_commits,
                model,
                buffer_percentage=buffer_percentage,
                joiner=COMMIT_BATCH_JOINER,
            )
        )

    logger.info(
        "Batched {commits} into {batches} for more efficient processing",
        commits=(
            f"{commits_count} commits"
            if commits_count > 1
            else f"{commits_count} commit"
        ),
        batches=(
            f"{batch_count} batches"
            if (batch_count := len(batched_chunks)) > 1
            else f"{batch_count} batch"
        ),
    )

    with Progress(
        SpinnerColumn(),
        "[progress.description]Processing GitHub commits",
        MofNCompleteColumn(),
        "[progress.percentage]({task.percentage:>3.0f}%)",
        "[progress.elapsed](Elapsed: {task.elapsed:.2f}s)",
    ) as progress:
        brag_document = await generate_brag_document(
            model_name,
            progress.track(batched_chunks),
            language=language,
        )

    # Open the output file if specified, otherwise use stdout
    if output:
        output.write_text(brag_document)
    else:
        print(brag_document)


@app.command
async def from_local(
    repo: Annotated[
        Path,
        cyclopts.Parameter(
            help="The path to the local repository to generate the brag document for.",
            group=inputs_group,
        ),
    ],
    author: Annotated[
        str,
        cyclopts.Parameter(
            name=("-u", "--user"),
            help="The user to generate the brag document for.",
            group=inputs_group,
        ),
    ],
    from_date: Annotated[
        datetime | None,
        cyclopts.Parameter(
            name="--from",
            help="The start date to generate the brag document for",
            group=inputs_group,
        ),
    ] = None,
    to_date: Annotated[
        datetime | None,
        cyclopts.Parameter(
            name="--to",
            help="The end date to generate the brag document for",
            group=inputs_group,
        ),
    ] = None,
    limit: Annotated[
        int | None,
        cyclopts.Parameter(
            help="The maximum number of commits to include in the brag document",
            group=inputs_group,
        ),
    ] = None,
    output: Annotated[
        Path | None,
        cyclopts.Parameter(
            name=("-o", "--output"),
            help="Path to save the commit history. Outputs Markdown-formatted text to stdout if not specified.",
            group=outputs_group,
        ),
    ] = None,
    overwrite: Annotated[
        bool,
        cyclopts.Parameter(
            name="--overwrite",
            help="If set, overwrites the output file if it already exists.",
            group=outputs_group,
        ),
    ] = False,
    model_name: Annotated[
        AvailableModelFullName,
        cyclopts.Parameter(
            name="--model",
            help=(
                "The name of the model to use for generating the brag document."
                " See `brag list-models` for the list of available models."
            ),
            group=model_group,
            show_choices=False,
        ),
    ] = "google-gla:gemini-2.0-flash",
    language: Annotated[
        str,
        cyclopts.Parameter(
            "--language",
            help="The language to use for generating the brag document.",
            group=model_group,
        ),
    ] = "english",
    buffer_percentage: Annotated[
        float,
        cyclopts.Parameter(
            help=(
                "The percentage of the model's context window to reserve as a buffer when batching commits."
                " Higher values (e.g., 0.3) are more conservative, while lower values (e.g., 0.1) allow for more chunks per batch but increase the risk of accidentally exceeding the limit."
            ),
            group=model_group,
        ),
    ] = 0.2,
) -> None:
    """Generate a brag document from a local Git repository.

    This command analyzes commits from a local Git repository specified by path,
    and then uses an AI model to generate a comprehensive brag document summarizing
    the user's contributions.

    Unlike the `from-repo` command which works with GitHub repositories, this command
    operates directly on a local Git repository and doesn't require a GitHub API token.
    This is useful for private repositories or repositories hosted on platforms other
    than GitHub.

    The command supports filtering commits by author, date range, and limiting the
    number of commits to process. The generated brag document is formatted in Markdown
    and can be saved to a file or printed to stdout.

    To optimize performance and avoid rate limiting issues, commits are batched together
    into larger chunks that fit within the model's context window. This significantly
    reduces the number of API calls to the LLM provider for repositories with many commits.

    The batching process uses token count estimation to determine how many commits
    can be combined safely. The `--buffer-percentage` parameter allows you to control
    how conservative this batching should be by reserving a portion of the model's
    context window as a safety buffer.
    """
    if output is not None and output.exists() and not overwrite:
        raise FileExistsError(
            f"Output file `{output}` already exists. Use `--overwrite` to overwrite."
        )

    if model_name not in AVAILABLE_MODEL_FULL_NAMES:
        raise ValueError(
            f"Model `{model_name}` is not available. See `brag list-models` for the list of available models."
        )

    repo = repo.resolve()

    model = Model.from_full_name(model_name)

    logger.info(
        "Generating brag document from {repo} for {author}{from_date}{to_date}",
        repo=repo,
        author=author,
        from_date=f" from {from_date}" if from_date else "",
        to_date=f" to {to_date}" if to_date else "",
    )

    git_commits: DataSource[GitCommit] = GitCommitsSource(
        path=repo,
        author=author,
        from_date=from_date,
        to_date=to_date,
    )
    if limit:
        git_commits = git_commits.limit(limit)

    commits_count = len(git_commits)

    logger.info(
        "Processing {commits} for {author} in {repo}",
        commits=(
            f"{commits_count} commits"
            if commits_count > 1
            else f"{commits_count} commit"
        ),
        author=author,
        repo=repo,
    )

    # Batch chunks to respect rate limits
    batched_chunks = tuple(
        batch_chunks_by_token_limit(
            git_commits,
            model,
            buffer_percentage=buffer_percentage,
            joiner=COMMIT_BATCH_JOINER,
        )
    )

    logger.info(
        "Batched {commits} into {batches} for more efficient processing",
        commits=(
            f"{commits_count} commits"
            if commits_count > 1
            else f"{commits_count} commit"
        ),
        batches=(
            f"{batch_count} batches"
            if (batch_count := len(batched_chunks)) > 1
            else f"{batch_count} batch"
        ),
    )

    with Progress(
        SpinnerColumn(),
        "[progress.description]Processing commits",
        MofNCompleteColumn(),
        "[progress.percentage]({task.percentage:>3.0f}%)",
        "[progress.elapsed](Elapsed: {task.elapsed:.2f}s)",
    ) as progress:
        brag_document = await generate_brag_document(
            model_name,
            progress.track(batched_chunks),
            language=language,
        )

    # Open the output file if specified, otherwise use stdout
    if output:
        output.write_text(brag_document)
    else:
        print(brag_document)


@app.command(
    name=(
        "list-models",
        "ls-models",
    )
)
def list_models(
    format: Annotated[
        Literal["text", "json"],
        cyclopts.Parameter(
            help="The format to use for the output.",
        ),
    ] = "text",
) -> None:
    """List all available models."""
    all_models = tuple(
        sorted(
            AVAILABLE_MODELS,
            key=lambda model: model.full_name,
        )
    )

    match format:
        case "text":
            grouped_models = groupby(all_models, key=lambda model: model.provider)
            for provider, models in grouped_models:
                print(f"{provider}:")
                for model in models:
                    print(f"  {model.name}")
        case "json":
            print(
                json.dumps(
                    [
                        {
                            "provider": model.provider,
                            "name": model.name,
                            "full_name": model.full_name,
                        }
                        for model in all_models
                    ]
                )
            )
