from pydantic import BaseModel,Field
from typing import List
from datetime import date



class   SalePersonBase(BaseModel):
    name : str
    contact : str
    class Config:
        orm_mode = True


class PurchaseBase(BaseModel):
    Date : date
    class Config:
        orm_mode = True