from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings

app = FastAPI(
    title="DishCraft",
    description="api to craft, store, manage recipes generated or manually added",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CREATE DATABASE TABLES

# TODO: ADD APP ROUTES HERE

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)