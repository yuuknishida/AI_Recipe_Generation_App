from http.client import parse_headers

from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

# ===========================================================================================================
# INGREDIENT SCHEMA
# ===========================================================================================================
class IngredientBase(BaseModel):
    name: str
    measurements: float
    units: str

class IngredientCreate(IngredientBase):
    pass

class IngredientResponse(IngredientBase):
    id: int

    class Config:
        from_attributes = True

# ===========================================================================================================
# INSTRUCTION SCHEMA
# ===========================================================================================================
class InstructionBase(BaseModel):
    step: int
    instruction: str
    cook_time: int

class InstructionCreate(InstructionBase):
    pass

class InstructionResponse(InstructionBase):
    id: int 

    class Config:
        from_attributes = True

# ===========================================================================================================
# CUISINE SCHEMA
# ===========================================================================================================
class CuisineBase(BaseModel):
    name: str

class CuisineCreate(CuisineBase):
    pass

class CuisineResponse(CuisineBase):
    id: int

    class Config:
        from_attributes = True

# ===========================================================================================================
# RECIPE SCHEMA
# ===========================================================================================================
class RecipeBase(BaseModel):
    name: str
    description: str
    cook_time: int
    prep_time: int
    calories: int
    image: str
    dietary: Optional[str] = None
    servings: int
    cuisine_id: int

class RecipeCreate(RecipeBase):
    ingredients: List[IngredientResponse]
    instructions: List[InstructionResponse]

class RecipeResponse(RecipeBase):
    id: int
    ingredients: List[IngredientResponse] = []
    instructions: List[InstructionResponse] = []
    cuisine: CuisineResponse

    class Config: 
        from_attributes = True