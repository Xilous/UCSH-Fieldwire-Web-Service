from pydantic_settings import BaseSettings
from functools import lru_cache
import os
from pathlib import Path

class Settings(BaseSettings):
    # Fieldwire API Configuration
    FIELDWIRE_ACCOUNT_ID: str
    FIELDWIRE_ACCESS_TOKEN: str
    FIELDWIRE_API_BASE_URL: str = "https://client-api.us.fieldwire.com/api/v3"
    FIELDWIRE_WEBHOOK_BASE_URL: str = "https://webhook-api.us.fieldwire.com/webhook/account"
    
    # Application Configuration
    PROJECTS_FILE: Path = Path("data/projects.json")
    
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings() -> Settings:
    return Settings() 