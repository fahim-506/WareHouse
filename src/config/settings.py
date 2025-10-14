
import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DB_URL")


settings = Settings()