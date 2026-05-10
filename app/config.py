from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    OLLAMA_MODEL: str = "mistral"
    CHROMA_PATH: str = "vector_store"
    COLLECTION_NAME: str = "healthcare_docs"
    EMBEDDING_MODEL: str = "BAAI/bge-small-en-v1.5"

    class Config:
        env_file = ".env"


settings = Settings()