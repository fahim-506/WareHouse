from pydantic import BaseModel,Field
from typing import List,Optional
from datetime import date
from src.schemas.product import ProductBase,ProductSectionBase


class SalePersonBase(BaseModel):
    name : str
    contact : str
    class Config:
        orm_mode = True


class PurchaseBase(BaseModel):
    person_name: str
    product_name: str
    product_section : int
    quantity : int
    date : date
    total_price: float
    class Config:
        orm_mode = True

#  Input model for creating a purchase
class PurchaseCreate(BaseModel):
    quantity: int
    date: date


class Purchases(BaseModel):
    id: int
    sale_person_id: int
    product_id: int
    product_section_id: int
    quantity: int
    date: date

    class Config:
        orm_mode = True
