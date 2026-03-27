from pydantic import BaseModel
from typing import Optional, List

class AIRecipeGenerateRequest(BaseModel):
    ingredients: Optional[List[str]]
    cuisine: Optional[str]
    prompt: Optional[str]
