from app.embeddings import get_retriever
from app.llm import generate_response


PROMPT_TEMPLATE = """
You are a healthcare assistant.

Answer ONLY from the provided context.

If answer is not found, say:
"I could not find this information in the provided documents."

Context:
{context}

Question:
{question}

Answer:
"""


def ask_question(question: str):
    retriever = get_retriever()

    docs = retriever.invoke(question)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = PROMPT_TEMPLATE.format(
        context=context,
        question=question
    )

    answer = generate_response(prompt)

    sources = [
        {
            "document": doc.metadata["source"],
            "chunk": doc.page_content[:250]
        }
        for doc in docs
    ]

    return {
        "answer": answer,
        "sources": sources
    }