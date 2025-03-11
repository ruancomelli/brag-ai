"""Model definitions for AI providers and their models.

This module provides a standardized way to represent and work with AI models
from different providers. It includes utilities for parsing model names,
validating them, and accessing available models.
"""

from collections.abc import Iterator
from typing import Self
from typing import get_args as get_literal_type_args

from pydantic import BaseModel, ConfigDict
from pydantic_ai.models import KnownModelName as _KnownModelName

type AvailableModelFullName = _KnownModelName
type ProviderName = str
type ModelName = str


class InvalidFullModelNameError(ValueError):
    """Raised when a full model name doesn't follow the 'provider:name' format."""

    def __init__(self, full_name: str) -> None:
        super().__init__(f"Invalid model name: {full_name}")


class Model(BaseModel):
    """Represents an AI model with its provider and name.

    Models are immutable and identified by a combination of provider and name.
    """

    model_config = ConfigDict(frozen=True)

    provider: ProviderName
    name: ModelName

    @property
    def full_name(self) -> str:
        """The full qualified name of the model in 'provider:name' format."""
        return f"{self.provider}:{self.name}"

    @classmethod
    def from_full_name(cls, full_name: str) -> Self:
        """Parse a full model name in 'provider:name' format into a Model instance."""
        try:
            provider, name = full_name.split(":")
        except ValueError as e:
            raise InvalidFullModelNameError(full_name) from e

        return cls(provider=provider, name=name)


def _iter_available_models() -> Iterator[Model]:
    """Iterate over all available models from pydantic-ai's known models.

    Skips models with invalid provider names.
    """
    known_models = get_literal_type_args(AvailableModelFullName)
    for model_name in known_models:
        try:
            yield Model.from_full_name(model_name)
        except InvalidFullModelNameError:
            # Some models in `pydantic-ai` don't have a valid provider name
            continue


AVAILABLE_MODELS = frozenset(_iter_available_models())
"""Frozen set of all available and valid AI models."""
