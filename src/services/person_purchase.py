from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.schemas import purchase
from src.models.purchase import Sale_Person
from typing import List, Dict


# ================= Sale Person =================

#create sale person
def Create_Saleperson(db : Session , person : purchase.SalePersonBase):
    # Sale_Person.contact & Sale_Person.name == person.contact & person.name
    existing = db.query(Sale_Person).filter(Sale_Person.contact==person.contact & Sale_Person.name==person.name).first()
    print(f": {existing}")
    if existing:
        return HTTPException(status_code=400, detail="This Sale person already exists")
    if(len(contact = person.contact) == 10):
        db_saleperson = Sale_Person(name = person.name , contact = person.contact)
        try:
            db.add(db_saleperson)
            db.commit()
            db.refresh(db_saleperson)
            return db_saleperson
        except Exception as e:
            db.rollback()
            return HTTPException(status_code=500, detail= f"Failed to Add Sale Person :{str(e)}")
        
    return f"please enter valid 10 digit contact number"