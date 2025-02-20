"""A model for generating a brag document from a list of documents."""

from typing import Literal, TypedDict

from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.runnables import RunnableConfig
from langchain_text_splitters import CharacterTextSplitter
from langgraph.graph import END, START, StateGraph

from brag.text_formatters import compose_text

StartType = Literal["__start__"]
EndType = Literal["__end__"]


def generate_brag_document(documents: list[Document]) -> str:
    """Generate a brag document from a list of documents."""
    graph = StateGraph(BragDocumentGenerationState)
    graph.add_node("generate_initial_summary", generate_initial_summary)
    graph.add_node("refine_summary", refine_summary)
    graph.add_edge(START, "generate_initial_summary")
    graph.add_conditional_edges("generate_initial_summary", should_refine)
    graph.add_conditional_edges("refine_summary", should_refine)
    app = graph.compile()

    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=1000, chunk_overlap=0
    )
    chunks = text_splitter.split_documents(documents)
    return app.invoke({"contents": chunks})


# Initial summary
summarize_prompt = ChatPromptTemplate(
    (
        HumanMessagePromptTemplate.from_template(
            "Write a concise summary of the following: {context}"
        ),
    )
)
initial_summary_chain = summarize_prompt | llm | StrOutputParser()

# Refining the summary with new docs
refine_template = compose_text(
    """
        Produce a final summary.

        Existing summary up to this point:
        {existing_answer}

        New context:
        ------------
        {context}
        ------------

        Given the new context, refine the original summary.
    """
)
refine_prompt = ChatPromptTemplate(
    (HumanMessagePromptTemplate.from_template(refine_template),)
)

refine_summary_chain = refine_prompt | llm | StrOutputParser()


# We will define the state of the graph to hold the document
# contents and summary. We also include an index to keep track
# of our position in the sequence of documents.
class BragDocumentGenerationState(TypedDict):
    contents: list[str]
    index: int
    summary: str


# We define functions for each node, including a node that generates
# the initial summary:
def generate_initial_summary(
    state: BragDocumentGenerationState,
) -> BragDocumentGenerationState:
    return {
        "contents": state["contents"],
        "summary": "",
        "index": 0,
    }


# And a node that refines the summary based on the next document
async def refine_summary(
    state: BragDocumentGenerationState,
    config: RunnableConfig,
):
    content = state["contents"][state["index"]]
    summary = await refine_summary_chain.ainvoke(
        {"existing_answer": state["summary"], "context": content},
        config,
    )

    return {"summary": summary, "index": state["index"] + 1}


# Here we implement logic to either exit the application or refine
# the summary.
def should_refine(
    state: BragDocumentGenerationState,
) -> Literal["refine_summary", EndType]:
    if state["index"] >= len(state["contents"]):
        return END
    else:
        return "refine_summary"


def calculate_token_count_of_documents(documents: list[Document]) -> int:
    """Calculate the token count of a list of documents."""
    return sum(llm.get_num_tokens(doc.page_content) for doc in documents)
