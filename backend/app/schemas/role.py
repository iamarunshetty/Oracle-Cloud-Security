"""Role Pydantic schemas."""

from datetime import datetime
from typing import Optional

from app.schemas.base import OrmBase


class RoleCreate(OrmBase):
    role_code: str
    role_name: str
    role_type: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None


class RoleUpdate(OrmBase):
    role_name: Optional[str] = None
    role_type: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None


class RoleResponse(OrmBase):
    id: str
    role_code: str
    role_name: str
    role_type: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    is_active: bool
    created_at: datetime
    updated_at: datetime
