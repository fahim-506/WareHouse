from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.schemas import purchase
from src.models.purchase import Sale_Person
from typing import List, Dict


# ================= Sale Person =================

#create sale person
def Create_Saleperson(db : Session , person : purchase.SalePersonBase):

    existing = db.query(Sale_Person).filter((Sale_Person.contact==person.contact) & (Sale_Person.name==person.name)).first()
    print(f"Existing: {existing}")
    if existing:
        return HTTPException(status_code=400, detail="This Sale person already exists")
    if len(str(person.contact)) == 10:
        db_saleperson = Sale_Person(name = person.name , contact = person.contact)
        try:
            db.add(db_saleperson)
            db.commit()
            db.refresh(db_saleperson)
            return db_saleperson
        except Exception as e:
            db.rollback()
            return HTTPException(status_code=500, detail= f"Failed to Add Sale Person :{str(e)}")
        
    else:
        raise HTTPException(status_code=422, detail="Please enter a valid 10-digit contact number.")
    

#get all sale person
def get_sale_person(db: Session):
    try:
        return db.query(Sale_Person).all()
    except Exception as e:
        return HTTPException(status_code=500, detail="error: "f"Failed to get all sale person : {str(e)}")
    
# get sale person by id 
def get_sale_person_by_id(sale_person : int ,db : Session):
    try:
        db_person = db.query(Sale_Person).filter(Sale_Person.id == sale_person).first()
        if not db_person:
            raise HTTPException(status_code=400, detail="Sale Person not found")
        return db_person
    except Exception as e:
        raise HTTPException(status_code=500, detail="error : " f"Failed to get sale person by id : {str(e)}")
    

#update sale person
def update_person(person_id : int, person: str, db : Session):
    try:
        db_person = db.query(Sale_Person).filter(Sale_Person.id == person_id).first()
        if not db_person:
            raise HTTPException(status_code=400, detail="sale person not found")
        db_person.name = person
        db_person.price = person
        db.commit()
        db.refresh(db_person)
        return db_person
    except Exception as e:
        raise HTTPException(status_code=500, detail="error : "f"Failed to update sale person: {str(e)}")
    

#Delete sale person
def delete_person(person_id : int , db: Session):
    try:
        db.query(Sale_Person).filter(Sale_Person.id == person_id).delete()
        db.commit()
    except Exception as e:
        print(f"Error in Delete sale person: {str(e)}")
        raise e


