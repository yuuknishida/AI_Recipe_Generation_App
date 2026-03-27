from sqlalchemy import Column, Integer, String, ForeignKey, Float, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

import enum

from db.database import Base

class Ingredient(Base):
    __tablename__ = "ingredients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    measurements = Column(Float, nullable=False)
    units = Column(String, nullable=False)

    recipe_id = Column(Integer, ForeignKey("recipes.id", ondelete="CASCADE"), nullable=False)
    recipe = relationship("Recipe", back_populates="ingredients")

class Instruction(Base):
    __tablename__ = "instructions"
    id = Column(Integer, primary_key=True, index=True)
    step = Column(Integer, nullable=False)
    instruction = Column(String, nullable=False)
    cook_time = Column(Integer, nullable=True)
    
    recipe_id = Column(Integer, ForeignKey("recipes.id", ondelete="CASCADE"), nullable=False)
    recipe = relationship("Recipe", back_populates="instructions")

class Cuisine(Base):
    __tablename__ = "cuisine"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)

    recipes = relationship("Recipe", back_populates="cuisine")

class Recipe(Base):
    __tablename__ = "recipes"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    cook_time = Column(Integer, nullable=False)         # in minutes
    prep_time = Column(Integer, nullable=False)         # in minutes
    calories = Column(Integer, nullable=False)
    image = Column(String, nullable=False)

    class DietaryType(str, enum.Enum):
        vegan = "vegan"
        vegetarian = "vegetarian"
        gluten_free = "gluten_free"
        none = "none"

    dietary = Column(Enum(DietaryType), nullable=True)
    servings = Column(Integer, nullable=False)

    ingredients = relationship("Ingredient", back_populates='recipe', cascade="all, delete-orphan", passive_deletes=True)
    instructions = relationship("Instruction", back_populates='recipe', cascade="all, delete-orphan", passive_deletes=True)

    cuisine_id = Column(Integer, ForeignKey("cuisine.id"), nullable=False)
    cuisine = relationship("Cuisine", back_populates="recipes")

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    user = relationship("User", back_populates="recipes")