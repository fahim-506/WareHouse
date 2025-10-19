from pydantic import BaseModel
from typing import List


class RackBase(BaseModel):
    name : str
    class Config:
        orm_mode = True


class SectionBase(BaseModel):
    name : str
    class Config:
        orm_mode = True


# class RackSectionBase(BaseModel):
#     id : int
#     rack : RackBase
#     section : SectionBase

#     class Config:
#         orm_mode = True