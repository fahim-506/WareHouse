from pydantic import BaseModel
from typing import List


class BrandBase(BaseModel):
    name : str

class BrandUpdate(BrandBase):
    pass

class CategoryBase(BaseModel):
    name : str


class ProductBase(BaseModel):
    name : str
    price : float


class ProductSectionBase(BaseModel):
    Quantity : str