# Healthcare AI Assistant (RAG-Based Clinical Policy Q&A)

A Retrieval-Augmented Generation (RAG) powered Healthcare AI Assistant built with FastAPI, ChromaDB, HuggingFace embeddings, and Ollama.

This system enables healthcare staff to query internal healthcare policy documents and receive grounded responses with source citations.

---

## Features

- Document ingestion pipeline for healthcare text files
- Semantic chunking and vector storage
- Retrieval-Augmented Generation (RAG)
- Local LLM inference using Ollama
- REST API with FastAPI
- Dockerized deployment
- Hallucination prevention
- Source-grounded answers
- Health monitoring endpoint

---

## Tech Stack

- Python
- FastAPI
- ChromaDB
- LangChain
- HuggingFace Embeddings
- Ollama (Mistral)
- Docker
- uv

---

## Architecture Diagram

![Architecture Diagram](assets/architecture.png)

---

## Setup

### Create Environment
```bash
uv venv
```

Activate:

Windows:
```bash
.venv\Scripts\activate
```

Install:
```bash
uv pip install -r requirements.txt
```

---

### Run Ollama
```bash
ollama pull mistral
ollama serve
```

---

### Ingest Documents
```bash
uv run python -m app.embeddings
```

---

### Run API
```bash
uv run uvicorn app.main:app --reload
```

---

## API Docs

Open:

http://127.0.0.1:8000/docs

---

## Docker

Build:
```bash
docker compose build
```

Run:
```bash
docker compose up
```

---

## Endpoints

### GET /health

Returns application health.

### POST /ingest

Ingests healthcare policy documents.

### POST /ask

Accepts natural language healthcare policy questions.

Example:
```json
{
  "question": "Can a patient request medication refill through telehealth?"
}
```

---

## Hallucination Prevention

Unsupported queries return:

> I could not find this information in the provided documents.

---

## Author

Developed for the Mindbowser Healthcare AI Assistant Assignment.

