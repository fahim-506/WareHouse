from pydantic import BaseModel
from typing import List
# from src.schemas.racksection import RackSectionBase

class BrandBase(BaseModel):
    name : str
    class Config:
        orm_mode = True

class BrandUpdate(BrandBase):
    pass

class CategoryBase(BaseModel):
    name : str
    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    name : str
    price : float
    class Config:
        orm_mode = True


class ProductSectionBase(BaseModel):
    quantity : int


    class Config:
        orm_mode = True



    # product: ProductBase
    # racksection: RackSectionBase