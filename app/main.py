from fastapi import FastAPI
from pydantic import BaseModel

from app.embeddings import ingest_documents
from app.rag import ask_question
from app.agent import route_question

app = FastAPI(title="Healthcare AI Assistant")


class QuestionRequest(BaseModel):
    question: str


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/ingest")
def ingest():
    ingest_documents()
    return {"message": "Documents ingested successfully"}


@app.post("/ask")
def ask(req: QuestionRequest):
    routed = route_question(req.question)

    if routed:
        return routed

    return ask_question(req.question)