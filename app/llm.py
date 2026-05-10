import ollama
import os
from app.config import settings

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://host.docker.internal:11434")


def generate_response(prompt: str) -> str:
    client = ollama.Client(host=OLLAMA_HOST)

    response = client.chat(
        model=settings.OLLAMA_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]