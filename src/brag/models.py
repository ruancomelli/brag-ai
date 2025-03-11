"""Model definitions for AI providers and their models.

This module provides a standardized way to represent and work with AI models
from different providers. It includes utilities for parsing model names,
validating them, and accessing available models.
"""

from collections.abc import Iterator
from typing import Final, Self
from typing import get_args as get_literal_type_args

from pydantic import BaseModel, ConfigDict
from pydantic_ai.models import KnownModelName as _KnownModelName

type AvailableModelFullName = _KnownModelName
type ProviderName = str
type ModelName = str
type TokenCount = int

CONTEXT_WINDOW_SIZES: Final[dict[AvailableModelFullName, TokenCount]] = {
    # ==========================================================
    # OpenAI
    # https://platform.openai.com/docs/models
    # ------------------------------------------------------------
    "openai:chatgpt-4o-latest": 128_000,
    "openai:gpt-3.5-turbo": 16_384,
    "openai:gpt-3.5-turbo-0125": 16_384,
    "openai:gpt-3.5-turbo-0301": 16_384,
    "openai:gpt-3.5-turbo-0613": 16_384,
    "openai:gpt-3.5-turbo-1106": 16_384,
    "openai:gpt-3.5-turbo-16k": 16_384,
    "openai:gpt-3.5-turbo-16k-0613": 16_384,
    "openai:gpt-4": 8_192,
    "openai:gpt-4-0125-preview": 8_192,
    "openai:gpt-4-0314": 8_192,
    "openai:gpt-4-0613": 8_192,
    "openai:gpt-4-1106-preview": 8_192,
    "openai:gpt-4-32k": 32_768,
    "openai:gpt-4-32k-0314": 32_768,
    "openai:gpt-4-32k-0613": 32_768,
    "openai:gpt-4-turbo": 128_000,
    "openai:gpt-4-turbo-2024-04-09": 128_000,
    "openai:gpt-4-turbo-preview": 128_000,
    "openai:gpt-4-vision-preview": 8_192,
    "openai:gpt-4o": 128_000,
    "openai:gpt-4o-2024-05-13": 128_000,
    "openai:gpt-4o-2024-08-06": 128_000,
    "openai:gpt-4o-2024-11-20": 128_000,
    "openai:gpt-4o-audio-preview": 128_000,
    "openai:gpt-4o-audio-preview-2024-10-01": 128_000,
    "openai:gpt-4o-audio-preview-2024-12-17": 128_000,
    "openai:gpt-4o-mini": 128_000,
    "openai:gpt-4o-mini-2024-07-18": 128_000,
    "openai:gpt-4o-mini-audio-preview": 128_000,
    "openai:gpt-4o-mini-audio-preview-2024-12-17": 128_000,
    "openai:o1": 128_000,
    "openai:o1-2024-12-17": 128_000,
    "openai:o1-mini": 20_000,
    "openai:o1-mini-2024-09-12": 20_000,
    "openai:o1-preview": 128_000,
    "openai:o1-preview-2024-09-12": 128_000,
    "openai:o3-mini": 200_000,
    "openai:o3-mini-2025-01-31": 200_000,
    # ==========================================================
    # Anthropic
    # https://docs.anthropic.com/en/docs/about-claude/models/all-models#model-comparison-table
    # ------------------------------------------------------------
    "anthropic:claude-3-5-haiku-latest": 200_000,
    "anthropic:claude-3-5-sonnet-latest": 200_000,
    "anthropic:claude-3-opus-latest": 200_000,
    # ==========================================================
    # Cohere
    # https://docs.cohere.com/docs/models
    # ------------------------------------------------------------
    "cohere:c4ai-aya-expanse-32b": 128_000,
    "cohere:c4ai-aya-expanse-8b": 8_000,
    "cohere:command": 4_000,
    "cohere:command-light": 4_000,
    "cohere:command-light-nightly": 4_000,
    "cohere:command-nightly": 128_000,
    "cohere:command-r": 128_000,
    "cohere:command-r-03-2024": 128_000,
    "cohere:command-r-08-2024": 128_000,
    "cohere:command-r-plus": 128_000,
    "cohere:command-r-plus-04-2024": 128_000,
    "cohere:command-r-plus-08-2024": 128_000,
    "cohere:command-r7b-12-2024": 128_000,
    # ==========================================================
    # Google
    # https://ai.google.dev/gemini-api/docs/models/gemini#model-variations
    # ------------------------------------------------------------
    "google-gla:gemini-1.5-flash": 1_048_576,
    "google-gla:gemini-1.5-flash-8b": 1_048_576,
    "google-gla:gemini-1.5-pro": 2_097_152,
    "google-gla:gemini-2.0-flash-exp": 1_048_576,
    "google-gla:gemini-2.0-flash-thinking-exp-01-21": 1_048_576,
    "google-gla:gemini-2.0-flash": 1_048_576,
    "google-gla:gemini-2.0-flash-lite-preview-02-05": 1_048_576,
    # ==========================================================
    # Groq
    # https://console.groq.com/docs/models
    # ------------------------------------------------------------
    "groq:gemma2-9b-it": 8_192,
    "groq:llama-3.1-8b-instant": 128_000,
    "groq:llama-3.2-11b-vision-preview": 128_000,
    "groq:llama-3.2-1b-preview": 128_000,
    "groq:llama-3.2-3b-preview": 128_000,
    "groq:llama-3.2-90b-vision-preview": 128_000,
    "groq:llama-3.3-70b-specdec": 8_192,
    "groq:llama-3.3-70b-versatile": 128_000,
    "groq:llama3-70b-8192": 8_192,
    "groq:llama3-8b-8192": 8_192,
    "groq:mixtral-8x7b-32768": 32_768,
    # ==========================================================
    # Mistral
    # https://docs.mistral.ai/models
    # ------------------------------------------------------------
    "mistral:codestral-latest": 256_000,
    "mistral:mistral-large-latest": 131_000,
    "mistral:mistral-moderation-latest": 8_000,
    "mistral:mistral-small-latest": 32_000,
}


class InvalidFullModelNameError(ValueError):
    """Raised when a full model name doesn't follow the 'provider:name' format."""

    def __init__(self, full_name: str) -> None:
        super().__init__(f"Invalid model name: {full_name}")


class MissingContextWindowSizeError(ValueError):
    """Raised when a model has no context window size."""

    def __init__(self, model_name: str) -> None:
        super().__init__(f"Model {model_name} has no known context window size.")


class Model(BaseModel):
    """Represents an AI model with its provider and name.

    Models are immutable and identified by a combination of provider and name.
    """

    model_config = ConfigDict(frozen=True)

    provider: ProviderName
    name: ModelName
    context_window_size: TokenCount

    @property
    def full_name(self) -> str:
        """The full qualified name of the model in 'provider:name' format."""
        return f"{self.provider}:{self.name}"

    @classmethod
    def from_full_name(cls, full_name: AvailableModelFullName) -> Self:
        """Parse a full model name in 'provider:name' format into a Model instance."""
        try:
            provider, name = full_name.split(":")
        except ValueError as e:
            raise InvalidFullModelNameError(full_name) from e

        try:
            context_window_size = CONTEXT_WINDOW_SIZES[full_name]
        except KeyError as e:
            raise MissingContextWindowSizeError(full_name) from e

        return cls(
            provider=provider,
            name=name,
            context_window_size=context_window_size,
        )


def _iter_available_models() -> Iterator[Model]:
    """Iterate over all available models from pydantic-ai's known models.

    Skips models with invalid provider names or unknown context window sizes.
    """
    known_models = get_literal_type_args(_KnownModelName)
    for model_name in known_models:
        try:
            yield Model.from_full_name(model_name)
        except (
            # Some models in `pydantic-ai` don't have a valid provider name
            InvalidFullModelNameError,
            # We need to know the context window size for the model
            MissingContextWindowSizeError,
        ):
            continue


AVAILABLE_MODELS = frozenset(_iter_available_models())
"""Frozen set of all available and valid AI models."""
AVAILABLE_MODEL_FULL_NAMES = frozenset(model.full_name for model in AVAILABLE_MODELS)
"""Frozen set of all available and valid AI model full names."""
