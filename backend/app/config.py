import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "CitySoul"
    VERSION: str = "1.0.0"
    API_PREFIX: str = "/api"
    
    # Qloo API
    QLOO_API_KEY: str = ""
    QLOO_API_BASE_URL: str = "https://hackathon.api.qloo.com/v2"
    
    # AI Provider
    LLM_API_KEY: str = ""
    LLM_PROVIDER: str = "gemini"  # "mock", "openai", "gemini", "anthropic"
    GEMINI_MODEL: str = "gemini-flash-lite-latest"
    
    # Database
    DATABASE_URL: str = "sqlite:///./citysoul.db"
    
    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    CORS_ORIGINS: str = "http://localhost:5173,http://127.0.0.1:5173"
    
    model_config = SettingsConfigDict(
        env_file=(
            os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), ".env"),
            ".env"
        ),
        extra="ignore"
    )

    @property
    def cors_origins_list(self) -> List[str]:
        return [origin.strip() for origin in self.CORS_ORIGINS.split(",") if origin.strip()]

settings = Settings()
