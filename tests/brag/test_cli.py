"""Tests for the CLI module."""

from datetime import datetime

import pytest

from brag.cli import _maybe_parse_datetime


@pytest.mark.parametrize(
    ("date_str", "expected"),
    (
        pytest.param(None, None, id="none"),
        pytest.param("", None, id="empty string"),
        pytest.param("2024-01-01", datetime(2024, 1, 1), id="ISO date"),
        pytest.param(
            "2024-12-31 23:59:59",
            datetime(2024, 12, 31, 23, 59, 59),
            id="ISO datetime",
        ),
        pytest.param("2024-06-15", datetime(2024, 6, 15), id="mid-year date"),
    ),
)
def test_maybe_parse_absolute_datetime_valid_inputs(
    date_str: str | None,
    expected: datetime | None,
) -> None:
    """Test _maybe_parse_datetime with valid inputs."""
    result = _maybe_parse_datetime(date_str)

    if expected is None:
        assert result is None
    else:
        assert result == expected


@pytest.mark.parametrize(
    "invalid_date_str",
    (
        "not a date",
        "invalid date string",
        "abc123",
        "2024-13-45",  # Invalid month/day
    ),
)
def test_maybe_parse_datetime_invalid_inputs(invalid_date_str: str) -> None:
    """Test _maybe_parse_datetime with invalid inputs raises ValueError."""
    with pytest.raises(ValueError) as exc_info:
        _maybe_parse_datetime(invalid_date_str)

    assert "Invalid date format" in str(
        exc_info.value
    ) or "Could not parse date" in str(exc_info.value)
    assert invalid_date_str in str(exc_info.value)


@pytest.mark.parametrize(
    "natural_language_date_str",
    (
        "1 day ago",
        "2 days ago",
        "1 week ago",
        "2 weeks ago",
        "1 month ago",
        "2 months ago",
        "1 year ago",
        "yesterday",
        "today",
        "tomorrow",
        "last week",
        "last month",
        "next week",
        "next month",
    ),
)
def test_maybe_parse_relative_datetime_natural_language_dates(
    natural_language_date_str: str,
) -> None:
    """Test that natural language dates are parsed correctly."""
    result = _maybe_parse_datetime(natural_language_date_str)
    assert isinstance(result, datetime)


@pytest.mark.parametrize(
    ("natural_language_date_str", "expected_parsed_date"),
    (
        ("2024-01-01", datetime(2024, 1, 1)),
        ("2024-06-15", datetime(2024, 6, 15)),
        ("2024-12-31", datetime(2024, 12, 31)),
        ("2024-01-01T00:00:00", datetime(2024, 1, 1, 0, 0, 0)),
        ("2024-01-01T12:30:45", datetime(2024, 1, 1, 12, 30, 45)),
    ),
)
def test_maybe_parse_datetime_iso_formats(
    natural_language_date_str: str,
    expected_parsed_date: datetime,
) -> None:
    """Test that ISO date formats are parsed correctly."""
    result = _maybe_parse_datetime(natural_language_date_str)
    assert result == expected_parsed_date
