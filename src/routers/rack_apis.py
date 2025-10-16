from fastapi import APIRouter, Request, Response , Depends, HTTPException
from fastapi.responses import JSONResponse
from src.config.database import get_db
from src.schemas.racksection import RackBase,SectionBase
from src.services import rack
from sqlalchemy.orm import Session
from typing import List


router = APIRouter()

# ================= Rack =================

# create rack 
@router.post("/rack",response_model = RackBase)
def Create_rack(racks : RackBase, db: Session = Depends(get_db)):
    return rack.Create_rack(db, racks)

# read all rack 
@router.get("/rack", response_model = List[RackBase])
def read_rack(db: Session = Depends(get_db)):
    try:
        res = rack.get_rack(db)
        # print(type(res))
        return res
    except Exception as e:
        return HTTPException(400, detail={"error": f"Error in read_rack{str(e)}"})

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


# ================= Section =================

# create section
@router.post("/section",response_model= SectionBase)
def Create_Section(rack_id : int ,sections : SectionBase, db : Session = Depends(get_db)):
    return rack.Create_section(rack_id ,db,sections)


@router.get("/section",response_model =List[SectionBase])
def read_rack(db: Session = Depends(get_db)):
    return rack.get_section(db)


# read section by id
@router.get("/section/{section_id}",response_model=SectionBase)
def read_section_by_id(section_id : int ,db: Session = Depends(get_db)):
    return rack.get_section_by(db, section_id)


#update section 
@router.put("/section/{section_id}", response_model=SectionBase)
def update_section_name(section_id : int, section_update : SectionBase, db: Session = Depends(get_db)):
    db_section = rack.update_section_name(db, section_id, section_update)
    if not db_section:
        raise HTTPException(status_code=404, detail="Section not found")
    return db_section


# delete section 
@router.delete("/section/{section_id}")
def delete_section(section_id : int , db : Session = Depends(get_db)):
    success = rack.delete_section(db,section_id)
    if not success:
        return {"error ": f"Section with id {section_id} not found"}
    return {"message ": f"Section with id {section_id} deleted successfully"}
