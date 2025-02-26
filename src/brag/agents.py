"""A model for generating a brag document from a list of documents."""

from collections.abc import Iterable, Iterator
from typing import TypeVar

from pydantic_ai import Agent
from pydantic_ai.models import KnownModelName

from brag.text_formatters import compose_text, dedent_triple_quote_string

_T = TypeVar("_T")


async def generate_brag_document(
    model_name: KnownModelName,
    chunks: Iterable[str],
) -> str:
    """Generate a brag document from a list of chunks.

    Each chunk is a string of text that represents a part of the document. For instance:

    - a GitHub Pull Request
    - a blog post
    - a research paper
    - ... and others

    The caller is responsible for providing the chunks in the correct order and formatting
    them as strings.

    Args:
        agent: The agent to use for generating the brag document.
        chunks: The data chunks to use for generating the brag document.
            This is expected to contain at least one chunk.
    """
    first_chunk, remaining_chunks = _head_and_tail(chunks)

    # Generate initial summary from the first chunk.
    initial_brag_document_generator_agent = Agent(
        model_name,
        model_settings={"temperature": 0.0},
        system_prompt=dedent_triple_quote_string(
            """
                You are a professional writer who specializes in creating brag documents.
                Your task is to generate a brag document from a list of documents.
            """
        ),
    )
    brag_document = await _generate_initial_brag_document(
        initial_brag_document_generator_agent,
        first_chunk,
    )

    # Iteratively refine the brag document with the remaining chunks
    brag_document_updater_agent = Agent(
        model_name,
        model_settings={"temperature": 0.0},
        system_prompt=dedent_triple_quote_string(
            """
                You are a professional writer who specializes in creating brag documents.
                Your task is to generate a brag document from a list of documents.
            """
        ),
    )
    for chunk in remaining_chunks:
        brag_document = await _update_brag_document(
            brag_document_updater_agent, brag_document, chunk
        )

    return brag_document


async def _generate_initial_brag_document(
    agent: Agent,
    chunk: str,
) -> str:
    """Generate an initial version of the brag document."""
    prompt_template = "Write a concise summary of the following: {context}"
    prompt = PromptTemplate.from_template(prompt_template)
    chain = LLMChain(llm=agent.llm, prompt=prompt, output_parser=StrOutputParser())
    return await chain.arun(context=chunk)


async def _update_brag_document(agent: Agent, brag_document: str, chunk: str) -> str:
    """Refine a summary with a new document using pydantic-ai."""
    refine_template = compose_text(
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
    )

    return await agent.run(refine_template, brag_document=brag_document, context=chunk)


def _head_and_tail(iterable: Iterable[_T]) -> tuple[_T, Iterator[_T]]:
    """Return the first element of an iterable and the remaining elements."""
    iterator = iter(iterable)
    head = next(iterator)
    return head, iterator
