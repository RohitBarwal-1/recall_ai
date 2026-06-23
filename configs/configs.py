from pydantic_settings import BaseSettings

class Configuration(BaseSettings):
    DATABASE_USERNAME: str
    DATABASE_PASSWORD: str
    DATABASE_NAME: str
    DATABASE_HOST: str
    EMBEDDING_MODEL: str
    LLM_URL: str

_settings = Configuration()

DATABASE_USERNAME = _settings.DATABASE_USERNAME
DATABASE_PASSWORD = _settings.DATABASE_PASSWORD
DATABASE_NAME = _settings.DATABASE_NAME
DATABASE_HOST = _settings.DATABASE_HOST
EMBEDDING_MODEL = _settings.EMBEDDING_MODEL
LLM_URL = _settings.LLM_URL