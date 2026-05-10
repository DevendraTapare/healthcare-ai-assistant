from pathlib import Path
import logging

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from app.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATA_DIR = Path("data")


def load_documents():
    documents = []

    txt_files = list(DATA_DIR.glob("*.txt"))

    if not txt_files:
        raise FileNotFoundError("No text files found in /data")

    logger.info(f"Found {len(txt_files)} text files")

    for file_path in txt_files:
        loader = TextLoader(
            str(file_path),
            encoding="utf-8"
        )

        docs = loader.load()

        for doc in docs:
            doc.metadata["source"] = file_path.name

        documents.extend(docs)

    return documents


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    return splitter.split_documents(documents)


def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name=settings.EMBEDDING_MODEL,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True}
    )


def ingest_documents():
    logger.info("Starting ingestion")

    documents = load_documents()
    chunks = split_documents(documents)

    embeddings = get_embeddings()

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=settings.CHROMA_PATH,
        collection_name=settings.COLLECTION_NAME
    )

    logger.info(f"Ingested {len(chunks)} chunks")

    return vectorstore


def get_retriever():
    embeddings = get_embeddings()

    vectorstore = Chroma(
        persist_directory=settings.CHROMA_PATH,
        embedding_function=embeddings,
        collection_name=settings.COLLECTION_NAME
    )

    return vectorstore.as_retriever(
        search_kwargs={"k": 4}
    )


if __name__ == "__main__":
    ingest_documents()