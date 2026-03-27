from typing import List, Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from core.security import get_current_user
from schemas.user import UserCreate, UserResponse
from models.users import User as UserModel

from db.database import get_db

router = APIRouter()
# ===============================================================================================
# GET USERS
# ===============================================================================================
@router.get("/users", response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)) -> List[UserResponse]:
    users = db.query(UserModel).all()
    return users

# ===============================================================================================
# GET USER BY ID
# ===============================================================================================
@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)) -> UserResponse:
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_user

# ===============================================================================================
# GET CURRENT USER
# ===============================================================================================
@router.get("/users/me", response_model=UserResponse)
def get_me(current_user: Annotated[UserModel, Depends(get_current_user)]):
    return current_user
# ===============================================================================================
# DELETE USER
# ===============================================================================================
@router.delete("/users/{user_id}", response_model=UserResponse)
def delete_user(user_id: int, db: Session = Depends(get_db)) -> UserModel:
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    db.delete(user)
    db.commit()
    return user