"""Nox configuration file."""

import nox

nox.needs_version = ">=2025.02.09"

PYPROJECT = nox.project.load_toml("pyproject.toml")
PYTHON_VERSIONS = nox.project.python_versions(PYPROJECT)


@nox.session(
    default=False,
    venv_backend="uv",
    reuse_venv=True,
)
def dev(session: nox.Session) -> None:
    """Set up a python development environment for the project."""
    session.run_install(
        "uv",
        "sync",
        "--all-groups",
        env={"VIRTUAL_ENV": ""},
    )
    session.run(
        "pre-commit",
        "install",
        external=True,
    )


@nox.session(
    venv_backend="uv",
    reuse_venv=True,
)
def test(session: nox.Session) -> None:
    """Run tests.

    If no arguments are provided, run all tests.
    """
    _install_dependency_group(session, "test")

    test_files = session.posargs
    if test_files:
        session.log("Running tests for files: {}".format(", ".join(test_files)))
    else:
        session.log("Running all tests")

    session.run("pytest", *test_files)


@nox.session(
    name="test-cov",
    venv_backend="uv",
    reuse_venv=True,
)
def test_cov(session: nox.Session) -> None:
    """Run tests with coverage checks."""
    _install_dependency_group(session, "test-cov")
    session.run("pytest", "--cov")


@nox.session(
    venv_backend="uv",
    reuse_venv=True,
)
def format(session: nox.Session) -> None:
    """Format code."""
    _install_dependency_group(session, "format")
    session.run("ruff", "format", *session.posargs)


@nox.session(
    venv_backend="uv",
    reuse_venv=True,
)
def lint(session: nox.Session) -> None:
    """Lint code."""
    _install_dependency_group(session, "lint")
    session.run("ruff", "check", "--fix", *session.posargs)


@nox.session(
    name="type-check",
    venv_backend="uv",
    reuse_venv=True,
)
def type_check(session: nox.Session) -> None:
    """Type-check code."""
    _install_dependency_group(session, "type-check")
    session.run("mypy", *session.posargs)


def _install_dependency_group(session: nox.Session, group: str) -> None:
    session.run_install(
        "uv",
        "sync",
        "--group",
        group,
        env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location},
    )
