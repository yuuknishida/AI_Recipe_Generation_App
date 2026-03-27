import os
from openai import OpenAI
from dotenv import load_dotenv
from schemas.ai import AIRecipeGenerateRequest
from core.config import settings

SYSTEM_PROMPT =  """You are a world-class master chef with deep knowledge of all global cuisines. Generate high-quality, realistic recipes.

Return ONLY valid JSON in this format: 
{
    "name": string, 
    "description": string, 
    "cook_time": int, 
    "prep_time": int, 
    "calories": int, 
    "servings": int,
    "dietary": string or null,
    "ingredients": [{"name": string, "measurements": float, "units": string}], 
    "instructions": [{"step": int, "instructions": string}] 
} 
For cook_time and prep_time, plase return as minutes.
"""
load_dotenv()

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def generate(prompt: str) -> dict:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

def build_prompt(request: AIRecipeGenerateRequest) -> str:
    parts = ["Generate a detailed recipe"]

    if request.cuisine:
        parts.append(f"for {request.cuisine} cuisince")
    if request.ingredients:
        ingredient_list = ", ".join(request.ingredients)
        parts = f"using these ingredients {ingredient_list}"
    if request.prompt:
        parts.append(f"Additional Notes: {request.prompt}")
    
    parts.append("""
        Return the recipe as JSON with these exact fields:
        - name (string)
        - description (string)
        - cook_time (integer, minutes)
        - prep_time (integer, minutes)
        - calories (integer)
        - servings (integer)
        - dietary: (string or null)
        - ingredients (list of {name, measurements, units})     
        - instructions (list of {step, instructions, cook_time (optional)})      

    """)

    return " ".join(parts)