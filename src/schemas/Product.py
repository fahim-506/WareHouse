from pydantic import BaseModel
from typing import List


class BrandBase(BaseModel):
    name : str


class CategoryBase(BaseModel):
    name : str


class ProductBase(BaseModel):
    name : str
    price : int


class ProductSectionBase(BaseModel):
    Quantity : str