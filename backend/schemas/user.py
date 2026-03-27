from pydantic import BaseModel, EmailStr, Field
from datetime import datetime, UTC
from functools import partial
from typing import List

from schemas.recipe import RecipeResponse

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(BaseModel):
    id: int
    is_active: bool | None = Field(default=True)
    created_at: datetime
    recipes: List[RecipeResponse] = []
    
    class Config:
        from_attributes = True