"""Users API endpoints."""

from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])


def _svc(db: Session = Depends(get_db)) -> UserService:
    return UserService(db)


@router.get("/", response_model=List[UserResponse])
def list_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    svc: UserService = Depends(_svc),
):
    return svc.list_users(skip=skip, limit=limit)


@router.get("/search", response_model=List[UserResponse])
def search_users(
    q: str = Query(..., min_length=1),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    svc: UserService = Depends(_svc),
):
    return svc.search_users(q, skip=skip, limit=limit)


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate, svc: UserService = Depends(_svc)):
    return svc.create_user(payload)


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: str, svc: UserService = Depends(_svc)):
    user = svc.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.patch("/{user_id}", response_model=UserResponse)
def update_user(user_id: str, payload: UserUpdate, svc: UserService = Depends(_svc)):
    user = svc.update_user(user_id, payload)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/{user_id}/lock", response_model=UserResponse)
def lock_user(user_id: str, svc: UserService = Depends(_svc)):
    user = svc.lock_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/{user_id}/unlock", response_model=UserResponse)
def unlock_user(user_id: str, svc: UserService = Depends(_svc)):
    user = svc.unlock_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/{user_id}/suspend", response_model=UserResponse)
def suspend_user(user_id: str, svc: UserService = Depends(_svc)):
    user = svc.suspend_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: str, svc: UserService = Depends(_svc)):
    if not svc.delete_user(user_id):
        raise HTTPException(status_code=404, detail="User not found")
