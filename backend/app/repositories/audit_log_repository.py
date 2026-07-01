"""AuditLog repository."""

from datetime import datetime
from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.audit_log import AuditLog
from app.repositories.base import BaseRepository


class AuditLogRepository(BaseRepository[AuditLog]):
    def __init__(self, db: Session) -> None:
        super().__init__(AuditLog, db)

    def search(
        self,
        actor_username: Optional[str] = None,
        action: Optional[str] = None,
        resource_type: Optional[str] = None,
        resource_id: Optional[str] = None,
        status: Optional[str] = None,
        from_date: Optional[datetime] = None,
        to_date: Optional[datetime] = None,
        skip: int = 0,
        limit: int = 100,
    ) -> List[AuditLog]:
        q = self.db.query(AuditLog)
        if actor_username:
            q = q.filter(AuditLog.actor_username.ilike(f"%{actor_username}%"))
        if action:
            q = q.filter(AuditLog.action == action)
        if resource_type:
            q = q.filter(AuditLog.resource_type == resource_type)
        if resource_id:
            q = q.filter(AuditLog.resource_id == resource_id)
        if status:
            q = q.filter(AuditLog.status == status)
        if from_date:
            q = q.filter(AuditLog.event_time >= from_date)
        if to_date:
            q = q.filter(AuditLog.event_time <= to_date)
        return q.order_by(AuditLog.event_time.desc()).offset(skip).limit(limit).all()
