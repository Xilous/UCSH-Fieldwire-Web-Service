from pydantic_settings import BaseSettings
from functools import lru_cache
from pathlib import Path

class Settings(BaseSettings):
    # Fieldwire API Configuration
    FIELDWIRE_ACCOUNT_ID: str = "1626878"
    FIELDWIRE_ACCESS_TOKEN: str = "fyWu9ulAJnutUewR88UUp8em61tCgs27Gya8Zcd8TrCJxy2YJLx6DHBcCz334K1I"
    FIELDWIRE_API_BASE_URL: str = "https://client-api.us.fieldwire.com/api/v3"
    FIELDWIRE_WEBHOOK_BASE_URL: str = "https://webhook-api.us.fieldwire.com/webhook/account"
    
    # Application Configuration
    PROJECTS_FILE: Path = Path("data/projects.json")

@lru_cache()
def get_settings() -> Settings:
    return Settings() 