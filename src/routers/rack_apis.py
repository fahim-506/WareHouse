from fastapi import APIRouter, Request, Response , Depends, HTTPException
from config.database import get_db
from schemas.racksection import RackBase,SectionBase
from services import rack
from sqlalchemy.orm import Session
from typing import List


router = APIRouter()

# create rack 
@router.post("/rack",response_model = RackBase)
def Create_rack(racks : RackBase, db: Session = Depends(get_db)):
    return rack.Create_rack(db, racks)

# read rack 
@router.get("/rack",response_model =List[RackBase])
def read_rack(db: Session = Depends(get_db)):
    return rack.get_rack(db)

# read rack by id
@router.get("/rack/{rack_id}",response_model =RackBase)
def read_rack_by_id(rack_id : int ,db: Session = Depends(get_db)):
    return rack.get_rack_by(db, rack_id)



# update rack
@router.put("/rack/{rack_id}/name",response_model = RackBase)
def update_rack_name(rack_id : int , rack_update : RackBase, db: Session = Depends(get_db)):
    db_rack = rack.update_rack_name(db, rack_id, rack_update)
    if not db_rack:
        raise HTTPException (status_code=404, detail="Rack name not found")
    return db_rack


#delete rack
@router.delete("/rack/{rack_id}")
def delete_rack(rack_id : int , db : Session = Depends(get_db)):
    success = rack.delete_rack(db, rack_id)
    if not success:
        return {"error ": f"Rack with id {rack_id} not found"}
    return {"message ": f"Rack with id {rack_id} deleted successfully"}


# create section
@router.post("/section",response_model= SectionBase)
def Create_Section(rack_id : int ,sections : SectionBase, db : Session = Depends(get_db)):
    return rack.Create_section(rack_id ,db,sections)


# @router.get("/timed")
# async def timed(rack_id: int):

# try
#     # user input data
#     # send to service/functions
#     # return the output
# excpt
#     return {"message": "It's the time of my life"}