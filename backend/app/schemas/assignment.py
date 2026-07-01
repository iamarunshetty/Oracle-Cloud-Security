"""UserRoleAssignment Pydantic schemas."""

from datetime import datetime
from typing import Optional

from app.schemas.base import OrmBase
from app.schemas.role import RoleResponse
from app.schemas.user import UserResponse


class AssignRoleRequest(OrmBase):
    user_id: str
    role_id: str
    assigned_by: Optional[str] = None
    expires_at: Optional[datetime] = None
    justification: Optional[str] = None


class RemoveRoleRequest(OrmBase):
    removed_by: Optional[str] = None


class AssignmentResponse(OrmBase):
    id: str
    user_id: str
    role_id: str
    assigned_by: Optional[str] = None
    assigned_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None
    removed_at: Optional[datetime] = None
    removed_by: Optional[str] = None
    approval_request_id: Optional[str] = None
    justification: Optional[str] = None
    created_at: datetime
    updated_at: datetime
