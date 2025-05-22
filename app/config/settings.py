from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    openai_api_key: str
    llm_model: str = "gpt-4o-mini"
    temperature: float = 0.7

    class Config:
        env_file = ".env"


settings = Settings()
