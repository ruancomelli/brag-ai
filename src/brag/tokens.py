"""Estimate the number of tokens in a text."""

import math
from typing import Literal, assert_never


def estimate_token_count(
    text: str,
    approximation_mode: Literal["underestimate", "overestimate"] = "overestimate",
) -> int:
    """Estimate the number of tokens in a text.

    This is a rough estimate and should only be used for rough comparisons.

    Args:
        text: The text to estimate the token count of.
        approximation_mode: The mode to use for the approximation.
            - "underestimate": Underestimate the token count. Useful to be conservative when avoiding hitting the context window limit.
            - "overestimate": Overestimate the token count. Useful to be generous when estimating the maximum number of tokens that can be used.
    """
    match approximation_mode:
        case "underestimate":
            return math.floor(len(text) / 5)
        case "overestimate":
            return math.ceil(len(text) / 3)
        case never:
            assert_never(never)
