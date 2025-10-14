from fastapi import APIRouter, Request, Response , Depends
from config.database import get_db
from schemas.racksection import RackBase
from services import rack
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/rack",response_model = RackBase)
def Create_rack(racks : RackBase, db: Session = Depends(get_db)):
    return rack.Create_rack(db, racks)

# @router.get("/timed")
# async def timed(rack_id: int):

# try
#     # user input data
#     # send to service/functions
#     # return the output
# excpt
#     return {"message": "It's the time of my life"}