from pydantic import BaseModel,Date,Field
from typing import List



class SalePersonBase(BaseModel):
    name : str
    contact : int = Field(...,  max_length=10)


class PurchaseBase(BaseModel):
    date : Date