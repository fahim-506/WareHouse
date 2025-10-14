
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from dotenv import load_dotenv
from src.config.settings import settings

load_dotenv()

engine = create_engine(settings.DATABASE_URL)
sessionlocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)



# def get_db():
#     try:
#         yield db
#     finally:
#         db.close()

        

