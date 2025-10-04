import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL :str = "postgresql://postgres:root@localhost:5432/inventory-db"

settings = Settings()