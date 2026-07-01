"""AuditLog Pydantic schemas."""

from datetime import datetime
from typing import Optional

from app.schemas.base import OrmBase


class AuditLogResponse(OrmBase):
    id: str
    event_time: datetime
    actor_id: Optional[str] = None
    actor_username: Optional[str] = None
    actor_ip: Optional[str] = None
    action: str
    resource_type: Optional[str] = None
    resource_id: Optional[str] = None
    resource_name: Optional[str] = None
    status: str
    detail: Optional[str] = None
    environment: Optional[str] = None
    tenant_id: Optional[str] = None


class AuditLogSearch(OrmBase):
    actor_username: Optional[str] = None
    action: Optional[str] = None
    resource_type: Optional[str] = None
    resource_id: Optional[str] = None
    status: Optional[str] = None
    from_date: Optional[datetime] = None
    to_date: Optional[datetime] = None
