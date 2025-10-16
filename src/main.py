from fastapi import FastAPI
import uvicorn
from src.routers.rack_apis  import router as rack_apis
from src.routers.product_details_apis  import router as product_apis
from src.routers.person_purchase_apis import router as purchase_apis
from src.config.database import engine,Base


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(rack_apis)
app.include_router(product_apis)
app.include_router(purchase_apis)



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
