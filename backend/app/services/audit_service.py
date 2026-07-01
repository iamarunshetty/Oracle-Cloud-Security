"""Audit log service."""

from datetime import datetime
from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.audit_log import AuditLog
from app.repositories.audit_log_repository import AuditLogRepository
from app.schemas.audit_log import AuditLogSearch


class AuditService:
    def __init__(self, db: Session) -> None:
        self.repo = AuditLogRepository(db)

    def log(
        self,
        action: str,
        actor_id: Optional[str] = None,
        actor_username: Optional[str] = None,
        actor_ip: Optional[str] = None,
        resource_type: Optional[str] = None,
        resource_id: Optional[str] = None,
        resource_name: Optional[str] = None,
        status: str = "SUCCESS",
        detail: Optional[str] = None,
        environment: Optional[str] = None,
        tenant_id: Optional[str] = None,
    ) -> AuditLog:
        entry = AuditLog(
            action=action,
            actor_id=actor_id,
            actor_username=actor_username,
            actor_ip=actor_ip,
            resource_type=resource_type,
            resource_id=resource_id,
            resource_name=resource_name,
            status=status,
            detail=detail,
            environment=environment,
            tenant_id=tenant_id,
        )
        return self.repo.create(entry)

    def list_logs(self, skip: int = 0, limit: int = 100) -> List[AuditLog]:
        return self.repo.list(skip=skip, limit=limit)

    def search_logs(
        self, search: AuditLogSearch, skip: int = 0, limit: int = 100
    ) -> List[AuditLog]:
        return self.repo.search(
            actor_username=search.actor_username,
            action=search.action,
            resource_type=search.resource_type,
            resource_id=search.resource_id,
            status=search.status,
            from_date=search.from_date,
            to_date=search.to_date,
            skip=skip,
            limit=limit,
        )
