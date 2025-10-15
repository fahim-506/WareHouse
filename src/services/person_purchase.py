from sqlalchemy.orm import Session
from fastapi import HTTPException
from schemas import purchase
from models.purchase import Sale_Person
from typing import List, Dict


#create sale person
def Create_Saleperson(db : Session , person : purchase.SalePersonBase):
    existing = db.query(Sale_Person).filter(Sale_Person.contact & Sale_Person.name == person.contact & person.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="This Sale person already exists")
    db_saleperson = Sale_Person(name = person.name , contact = person.contact)
    try:
        db.add(db_saleperson)
        db.commit()
        db.refresh(db_saleperson)
        return db_saleperson
    except Exception as e:
        db.rollback()
        return HTTPException(status_code=500, detail= f"Failed to create Sale Person :{str(e)}")
    