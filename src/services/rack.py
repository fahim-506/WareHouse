from sqlalchemy.orm import Session
from fastapi import HTTPException
from schemas import racksection
from models.rack_section import Rack
from typing import List, Dict


# {
#     "result" : "rspns"
# }


# func
# create rack name

# id
# section name
# id
# join the 

#create rack
def Create_rack (db : Session, rack : racksection.RackBase):
    existing = db.query(Rack).filter(Rack.name == rack.name).first()
    if existing:
        raise HTTPException(status_code = 400, detail = " Rack with same this same name is already exists")
    
    db_Rack = Rack(name = rack.name)
    try:
        db.add(db_Rack)
        db.commit()
        db.refresh(db_Rack)
        return db_Rack
    except Exception as e:
        db.rollback()
        raise HTTPException (status_code = 500 , detail= f"Failed to create Rack : {str(e)}")








