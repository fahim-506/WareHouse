from pydantic import BaseModel
from typing import List


class RackBase(BaseModel):
    name : str


class SectionBase(BaseModel):
    name : str