from sqlalchemy.orm import Session
from fastapi import HTTPException
from schemas import racksection
from models.rack_section import Rack, Section, RackSection
from typing import List, Dict


#create rack
def Create_rack (db : Session, rack : racksection.RackBase):
    existing = db.query(Rack).filter(Rack.name == rack.name).first()
    if existing:
        raise HTTPException(status_code = 400, detail = " This rack name is already exists")
    
    db_Rack = Rack(name = rack.name)
    try:
        db.add(db_Rack)
        db.commit()
        db.refresh(db_Rack)
        return db_Rack
    except Exception as e:
        db.rollback()
        raise HTTPException (status_code = 500 , detail= f"Failed to create Rack : {str(e)}")

#read rack
def get_rack(db : Session):
    return db.query(Rack).all()

# read rack by id
def get_rack_by(db : Session, rack_id : int ):
    db_rack_id = db.query(Rack).filter(Rack.id == rack_id).first()
    if not db_rack_id:
        raise HTTPException(status_code=400, detail="rack not found")
    # section new name add
    # racksection (section id, rack_id)
    # insert into rack section
    return db_rack_id


#update rack
def update_rack_name(db : Session, rack_id : int ,rack_update : racksection.RackBase):
    db_name = db.query(Rack).filter(Rack.id == rack_id).first()
    if not db_name:
        return None
    db_name.name = rack_update.name
    db.commit()
    db.refresh(db_name)
    return db_name


#delete rack
def delete_rack(db : Session, rack_id : int ):
    db_rack = db.query(Rack).filter(Rack.id == rack_id).first()
    if db_rack:
        db.delete(db_rack)
        db.commit()
        return True
    return False



# #Create Section
def Create_section(rack_id : int ,db: Session, section : racksection.SectionBase):
    db_rack = db.query(Rack).filter(Rack.id == rack_id).first()
    if not db_rack:
        raise HTTPException(status_code=400, detail="rack not found")
    
    existing = db.query(Section).filter(Section.name == section.name).first()
    if existing:
        raise HTTPException(status_code = 400, detail = " This Section name is already exists")
    
    try:
        db_Section = Section(name = section.name)
        db.add(db_Section)
        db.commit()
        db.refresh(db_Section)
        # print("section")
        # print(f"db_rack :: {db_rack.id}, db_Section: {db_Section.id}")
        db_racksection = RackSection(rack_id = db_rack.id , section_id = db_Section.id)
        # print(f"db_racksection :: {db_racksection}")
        db.add(db_racksection)
        db.commit()
        db.refresh(db_racksection)
        return db_Section
    except Exception as e:
        db.rollback()
        raise HTTPException (status_code = 500 , detail= f"Failed to create Section : {str(e)}")
