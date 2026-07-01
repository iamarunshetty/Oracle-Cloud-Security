"""User Pydantic schemas."""

from datetime import datetime
from typing import Optional

from pydantic import EmailStr

from app.schemas.base import OrmBase


class UserCreate(OrmBase):
    username: str
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    display_name: Optional[str] = None
    department: Optional[str] = None
    job_title: Optional[str] = None
    employee_id: Optional[str] = None
    fusion_user_id: Optional[str] = None
    notes: Optional[str] = None


class UserUpdate(OrmBase):
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    display_name: Optional[str] = None
    department: Optional[str] = None
    job_title: Optional[str] = None
    employee_id: Optional[str] = None
    is_active: Optional[bool] = None
    is_locked: Optional[bool] = None
    is_suspended: Optional[bool] = None
    notes: Optional[str] = None


class UserResponse(OrmBase):
    id: str
    fusion_user_id: Optional[str] = None
    username: str
    email: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    display_name: Optional[str] = None
    department: Optional[str] = None
    job_title: Optional[str] = None
    employee_id: Optional[str] = None
    is_active: bool
    is_locked: bool
    is_suspended: bool
    last_sync_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime
