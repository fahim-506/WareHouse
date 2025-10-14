
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from dotenv import load_dotenv
from config.settings import settings
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

engine = create_engine(settings.DATABASE_URL)
sessionlocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

Base = declarative_base()


def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

        

