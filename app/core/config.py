from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "GramAI"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    API_PREFIX: str = "/api/v1"

    MONGODB_URL: str = "mongodb://localhost:27017"
    MONGODB_DATABASE: str = "gramai"

    REDIS_URL: str = "redis://localhost:6379"

    QDRANT_URL: str = "http://localhost:6333"
    QDRANT_API_KEY: str | None = None

    OLLAMA_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "phi3"

    OPENAI_API_KEY: str | None = None
    OPENAI_MODEL: str = "gpt-4o-mini"

    JWT_SECRET: str = "change-this-secret"
    JWT_ALGORITHM: str = "HS256"

    RATE_LIMIT_PER_MINUTE: int = 60

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()