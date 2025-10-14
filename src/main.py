from fastapi import  FastAPI
from src.routers.rack_apis import router
from src import models
from src.config.database import engine,sessionlocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
