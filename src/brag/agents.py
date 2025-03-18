"""A model for generating a brag document from a list of documents."""

from collections.abc import Iterable, Iterator
from functools import cache
from typing import TypeVar

from pydantic_ai import Agent
from pydantic_ai.models import KnownModelName

from brag.text_formatters import promptify

_T = TypeVar("_T")


async def generate_brag_document(
    model_name: KnownModelName,
    chunks: Iterable[str],
    language: str = "english",
) -> str:
    """Generate a brag document from a list of text chunks.

    This function takes a list of text chunks, each representing a contribution or achievement,
    and uses an AI agent to generate a comprehensive brag document. The brag document
    highlights the user's accomplishments, technical skills, and contributions.

    Each chunk is a string of text that represents a part of the document. Examples include:

    - GitHub Pull Requests
    - Blog posts
    - Research papers
    - Meeting notes
    - Project reports

    The caller is responsible for providing the chunks in the correct order and formatted in
    a sensible manner.

    Args:
        model_name: The name of the AI model to use for generating the brag document.
        chunks: An iterable of strings, where each string is a chunk of text
            representing a contribution or achievement. This is expected to contain at
            least one chunk.
        language: The language in which to generate the brag document.

    Returns:
        A string containing the generated brag document.

    """
    first_chunk, remaining_chunks = _head_and_tail(chunks)

    # Generate initial summary from the first chunk.
    initial_brag_document_generator_agent = _build_agent_from_system_prompt(
        model_name,
        system_prompt=f"""
            You are an expert in creating compelling brag documents that highlight a person's achievements and skills.
            Your task is to analyze a document and extract key accomplishments, technical skills demonstrated, and contributions made.
            Focus on quantifiable results and impactful contributions.
            Present the information in a concise and engaging manner, suitable for showcasing the individual's value.
            Return only the generated brag document without extra comments or code fences.
            Generate the brag document in {language}.
        """,
    )
    brag_document = await _generate_initial_brag_document(
        initial_brag_document_generator_agent,
        first_chunk,
    )

    # Iteratively refine the brag document with the remaining chunks
    for chunk in remaining_chunks:
        brag_document_updater_agent = _build_agent_from_system_prompt(
            model_name,
            system_prompt=f"""
                You are an expert in refining existing brag documents by incorporating new information.
                Your task is to integrate new context into an existing brag document, ensuring that the document remains concise, engaging, and highlights the individual's key achievements and skills.
                Focus on seamlessly weaving in new accomplishments, technical skills, and contributions, while maintaining a consistent tone and style.
                Return only the generated brag document without extra comments or code fences.
                Generate the brag document in {language}.
            """,
        )
        brag_document = await _update_brag_document(
            brag_document_updater_agent, brag_document, chunk
        )

    return brag_document


async def _generate_initial_brag_document(
    agent: Agent,
    chunk: str,
) -> str:
    """Generate an initial version of the brag document.

    This function takes a single text chunk and uses an AI agent to generate an
    initial version of the brag document.

    Args:
        agent: The AI agent to use for generating the initial brag document.
        chunk: A string of text representing the first contribution or achievement.

    Returns:
        A string containing the initial version of the brag document.

    """
    prompt = _generate_initial_brag_document_prompt(chunk)
    result = await agent.run(prompt)
    return result.data


def _generate_initial_brag_document_prompt(chunk: str) -> str:
    """Generate the prompt for the initial version of the brag document.

    This function generates the prompt that will be used to generate the initial
    brag document.  The prompt instructs the AI to generate a brag document from
    the given context.

    Args:
        chunk: A string of text representing the first contribution or achievement.

    Returns:
        A string containing the prompt for generating the initial brag document.

    """
    return promptify(
        """
            Generate a brag document from the following context:
            <context>
            {context}
            </context>
        """
    ).format(context=chunk)


async def _update_brag_document(
    agent: Agent,
    current_brag_document: str,
    new_context: str,
) -> str:
    """Refine a brag document with new context.

    This function takes an existing brag document and a new text chunk, and uses
    an AI agent to refine the brag document by incorporating the information from
    the new chunk.

    Args:
        agent: The AI agent to use for refining the brag document.
        current_brag_document: A string containing the existing brag document.
        new_context: A string of text representing the new contribution or achievement to incorporate.

    Returns:
        A string containing the refined brag document.

    """
    prompt = _generate_update_brag_document_prompt(current_brag_document, new_context)
    result = await agent.run(prompt)
    return result.data


def _generate_update_brag_document_prompt(
    current_brag_document: str,
    new_context: str,
) -> str:
    """Refine a summary with a new document.

    This function generates the prompt that will be used to refine the brag
    document. The prompt instructs the AI to incorporate the new context into
    the existing brag document, ensuring that the document remains concise,
    engaging, and highlights the individual's key achievements and skills.

    Args:
        current_brag_document: A string containing the existing brag document.
        new_context: A string of text representing the new contribution or
            achievement to incorporate.

    Returns:
        A string containing the prompt for refining the brag document.

    """
    return promptify(
        """
            Produce a refined brag document.

            Existing brag document up to this point:
            <brag_document>
            {brag_document}
            </brag_document>

            New context:
            <context>
            {context}
            </context>

            Given the new context, refine the original brag document.
        """
    ).format(brag_document=current_brag_document, context=new_context)


@cache
def _build_agent_from_system_prompt(
    model_name: KnownModelName,
    system_prompt: str,
) -> Agent:
    return Agent(
        model_name,
        model_settings={"temperature": 0.0},
        system_prompt=promptify(system_prompt),
    )


def _head_and_tail(iterable: Iterable[_T]) -> tuple[_T, Iterator[_T]]:
    """Return the first element of an iterable and the remaining elements, similar to `(head, *tail) = iterable`.

    This helper function takes an iterable and returns a tuple containing the first element and an iterator over the
    remaining elements.

    Args:
        iterable: An arbitrary iterable.

    Returns:
        A tuple `(head, tail)` containing the first element of the iterable and an iterator over
        the remaining elements.

    Raises:
        StopIteration: If the iterable is empty.

    """
    iterator = iter(iterable)
    head = next(iterator)
    return head, iterator
