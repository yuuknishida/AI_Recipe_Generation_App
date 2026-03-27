from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.security import get_current_user
from schemas.ai import AIRecipeGenerateRequest
from schemas.recipe import RecipeResponse
from services.ai import build_prompt, generate
from models.user import User
from models.recipe import Recipe
from db.database import get_db

router = APIRouter()

@router.post("/generate")
async def generate_recipe(request: AIRecipeGenerateRequest, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    prompt = build_prompt(request)
    recipe_data = await generate(prompt)

    recipe = Recipe(**recipe_data, user_id=current_user.id)
    db.add(recipe)
    db.commit()
    db.refresh(recipe)
    
    return recipe