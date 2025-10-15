from fastapi import FastAPI
import uvicorn
from routers.rack_apis  import router
from models import rack_section,product,purchase 
from config.database import engine,Base
from sqlalchemy.orm import Session

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
