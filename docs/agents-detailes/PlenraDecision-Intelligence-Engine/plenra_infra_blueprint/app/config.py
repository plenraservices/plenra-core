from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "plenra-core"
    app_env: str = "development"
    log_level: str = "INFO"
    api_prefix: str = "/v1"
    database_url: str = "postgresql+psycopg://postgres:postgres@localhost:5432/plenra"
    redis_url: str = "redis://localhost:6379/0"
    openai_api_key: str | None = None
    default_llm_model: str = "gpt-5-mini"
    secret_key: str = "change-me"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
