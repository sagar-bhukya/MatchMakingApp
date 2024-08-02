from pydantic import BaseModel,EmailStr
from typing import List

class UserBase(BaseModel):
    name: str
    age: int
    gender: str
    city: str
    interests: List[str]

class UserCreate(UserBase):
    email:EmailStr

class UserUpdate(UserBase):
    email:EmailStr


class User(UserBase):
    id: int
    email:EmailStr

    class Config:
        orm_mode = True

