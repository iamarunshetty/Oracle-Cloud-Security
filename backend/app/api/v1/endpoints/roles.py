"""Roles API endpoints."""

from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.role import RoleCreate, RoleResponse, RoleUpdate
from app.services.role_service import RoleService

router = APIRouter(prefix="/roles", tags=["Roles"])


def _svc(db: Session = Depends(get_db)) -> RoleService:
    return RoleService(db)


@router.get("/", response_model=List[RoleResponse])
def list_roles(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    svc: RoleService = Depends(_svc),
):
    return svc.list_roles(skip=skip, limit=limit)


@router.get("/search", response_model=List[RoleResponse])
def search_roles(
    q: str = Query(..., min_length=1),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    svc: RoleService = Depends(_svc),
):
    return svc.search_roles(q, skip=skip, limit=limit)


@router.post("/", response_model=RoleResponse, status_code=status.HTTP_201_CREATED)
def create_role(payload: RoleCreate, svc: RoleService = Depends(_svc)):
    return svc.create_role(payload)


@router.get("/{role_id}", response_model=RoleResponse)
def get_role(role_id: str, svc: RoleService = Depends(_svc)):
    role = svc.get_role(role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role


@router.patch("/{role_id}", response_model=RoleResponse)
def update_role(role_id: str, payload: RoleUpdate, svc: RoleService = Depends(_svc)):
    role = svc.update_role(role_id, payload)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role


@router.delete("/{role_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_role(role_id: str, svc: RoleService = Depends(_svc)):
    if not svc.delete_role(role_id):
        raise HTTPException(status_code=404, detail="Role not found")
