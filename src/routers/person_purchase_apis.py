from fastapi import APIRouter, Request, Response , Depends, HTTPException
from config.database import get_db
from schemas.purchase import SalePersonBase
from services import person_purchase
from sqlalchemy.orm import Session
from typing import List

router = APIRouter()

#create sale person
@router.post("/sale_person",response_model=SalePersonBase)
def Create_Saleperson(persons : SalePersonBase, db: Session = Depends(get_db)):
    return person_purchase.Create_Saleperson(db, persons)