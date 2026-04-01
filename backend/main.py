from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings
from db.database import create_tables
from router.user import router as user_router
from router.recipe import router as recipe_router
from router.auth import router as auth_router

app = FastAPI(
    title="DishCraft",
    description="api to craft, store, manage recipes generated or manually added",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)



app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# CREATE DATABASE TABLES
create_tables()

# TODO: ADD APP ROUTES HERE
app.include_router(user_router)
app.include_router(recipe_router)
app.include_router(auth_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)