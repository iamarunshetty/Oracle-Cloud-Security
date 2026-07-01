"""Role assignments API endpoints."""

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.assignment import AssignmentResponse, AssignRoleRequest, RemoveRoleRequest
from app.services.assignment_service import AssignmentService

router = APIRouter(prefix="/assignments", tags=["Role Assignments"])


def _svc(db: Session = Depends(get_db)) -> AssignmentService:
    return AssignmentService(db)


@router.post("/", response_model=AssignmentResponse, status_code=status.HTTP_201_CREATED)
def assign_role(payload: AssignRoleRequest, svc: AssignmentService = Depends(_svc)):
    """Assign a role to a user (idempotent — returns existing if already assigned)."""
    return svc.assign_role(payload)


@router.delete("/{user_id}/roles/{role_id}", response_model=AssignmentResponse)
def remove_role(
    user_id: str,
    role_id: str,
    payload: RemoveRoleRequest,
    svc: AssignmentService = Depends(_svc),
):
    """Soft-remove a role assignment from a user."""
    assignment = svc.remove_role(user_id, role_id, removed_by=payload.removed_by)
    if not assignment:
        raise HTTPException(
            status_code=404, detail="Active assignment not found for this user/role pair"
        )
    return assignment


@router.get("/{user_id}/roles", response_model=List[AssignmentResponse])
def list_user_assignments(user_id: str, svc: AssignmentService = Depends(_svc)):
    """List all active role assignments for a user."""
    return svc.list_user_assignments(user_id)
