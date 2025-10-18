from fastapi import APIRouter, Request, Response , Depends, HTTPException
from fastapi.responses import JSONResponse
from src.config.database import get_db
from src.schemas.purchase import SalePersonBase
from src.services import person_purchase
from sqlalchemy.orm import Session
from typing import List

router = APIRouter()

#create sale person
@router.post("/sale_person",response_model=SalePersonBase)
def Create_Saleperson(persons : SalePersonBase, db: Session = Depends(get_db)):
    return person_purchase.Create_Saleperson(db, persons)


#get all sale person
@router.get("/sale_person",response_model=List[SalePersonBase])
def get_sale_person(db:SalePersonBase=Depends(get_db)):
    return person_purchase.get_sale_person(db)

# get sale person by id 
@router.get("/sale_person/{id}",response_model=SalePersonBase)
def get_sale_person_by_id(sale_person : int, db:Session=Depends(get_db)):
    return person_purchase.get_sale_person_by_id(sale_person,db)

#update sale person
@router.put("/sale_person",response_model=SalePersonBase)
def update_sale_person(person_id : int ,person : SalePersonBase, db : Session = Depends(get_db)):
    db_person = person_purchase.update_person(db,person_id,person.name)
    if not db_person:
        return HTTPException(status_code=404, detail="Category not found")
    return db_person
    

#Delete sale person
@router.delete("/sale_person/{id}")
def delete_person(person_id : int ,db :Session=Depends(get_db),):
    try:
        person_purchase.delete_person(person_id,db)
        return JSONResponse({"message": "delete sucessfully"}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=404,detail="error :" f"Error in deleting: {str(e)}")
