from pydantic import BaseModel,Field
from typing import List
from datetime import date



class SalePersonBase(BaseModel):
    name : str
    contact : int


class PurchaseBase(BaseModel):
    Date : date