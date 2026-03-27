from http.client import ResponseNotReady
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from models.user import User as UserModel
from schemas.recipe import (
    IngredientCreate, IngredientResponse, InstructionCreate, InstructionResponse, RecipeCreate, RecipeResponse
)
from models.recipe import (
    Ingredient,
    Instruction,
    Cuisine,
    Recipe
)

from db.database import get_db

router = APIRouter()

# ===============================================================================================
# CREATE INGREDIENT
# ===============================================================================================
def create_ingredient(request: IngredientCreate, db: Session=Depends(get_db)) -> IngredientResponse:
    db_ingredient = db.query(Ingredient).filter(Ingredient.name == request.name).first()
    if db_ingredient:
        raise HTTPException(status_code=400)
    new_ingredient = Ingredient(**request.model_dump())
    db.add(new_ingredient)
    db.commit()
    db.refresh(new_ingredient)
    return new_ingredient
# ===============================================================================================
# DELETE INGREDIENT
# ===============================================================================================

# ===============================================================================================
# CREATE INSTRUCTION
# ===============================================================================================

def create_instruction(request: InstructionCreate, db: Session=Depends(get_db)) -> InstructionResponse:
    db_instruction = db.query(Instruction).filter(Instruction.instruction == request.instruction).first()
    if db_instruction:
        raise HTTPException(status_code=400)
    new_instruction = Instruction(**request.model_dump())
    db.add(new_instruction)
    db.commit()
    db.refresh(new_instruction)
    return new_instruction
# ===============================================================================================
# CREATE CUISINE
# ===============================================================================================
# def create_cuisine(request: CuisineCreate, db: Session=Depends(get_db)) -> CuisineResponse:
#     db_cuisine = db.query(Cuisine).filter(Cuisine.name == request.name).first()
#     if db_cuisine:
#         raise HTTPException(status_code=400)
#     new_cuisine = Cuisine(**request.model_dump())
#     db.add(new_cuisine)
#     db.commit()
#     db.refresh(new_cuisine)
#     return new_cuisine
# ===============================================================================================
# CREATE RECIPE
# ===============================================================================================
@router.post("/users/{user_id}/recipes", response_model=RecipeResponse)
def create_recipe(user_id: int, request: RecipeCreate, db: Session = Depends(get_db)) -> RecipeResponse:
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    new_recipe = Recipe(
        name=request.name,
        description=request.description,
        cook_time=request.cook_time,
        prep_time=request.prep_time,
        calories=request.calories,
        image=request.image,
        dietary=request.dietary,
        servings=request.servings,
        cuisine=Cuisine(name=request.cuisine.name),
        user_id=user_id,
        ingredients=[
            Ingredient(
                name=i.name,
                measurements=i.measurements,
                units=i.units
            )
            for i in request.ingredients
        ],
        instructions=[
            Instruction(
                step=i.step,
                instruction=i.instruction,
            )
            for i in request.instructions
        ]
    )
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)
    return new_recipe

# ===============================================================================================
# DELETE RECIPE
# ===============================================================================================
@router.delete("/users/{user_id}/recipes/{recipe_id}", response_model=RecipeResponse)
def delete_recipe(user_id: int, recipe_id: int, db: Session = Depends(get_db)) -> Recipe:
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id, Recipe.user_id == user_id).first()
    if not recipe:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found for this user")
    
    db.delete(recipe)
    db.commit()
    return recipe

# ===============================================================================================
# GET RECIPES FOR USER
# ===============================================================================================
@router.get("/users/{user_id}/recipes/", response_model=List[RecipeResponse])
def get_recipes_for_user(user_id: int, db: Session = Depends(get_db)) -> List[Recipe]:
    recipes = db.query(Recipe).filter(Recipe.user_id == user_id).all()
    if not recipes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipes not found for this user")
    return recipes
    
# ===============================================================================================
# GET RECIPE FOR USER
# ===============================================================================================
@router.get("/users/{user_id}/recipes/{recipe_id}", response_model=RecipeResponse)
def get_recipe_for_user(user_id: int, recipe_id: int, db: Session = Depends(get_db)) -> Recipe:
    recipe = db.query(Recipe).filter(Recipe.user_id == user_id, Recipe.id == recipe_id).first()
    
    if not recipe:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found for this user")
    
    return recipe