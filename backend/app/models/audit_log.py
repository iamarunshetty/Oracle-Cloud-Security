"""AuditLog ORM model — immutable, append-only audit trail."""

import uuid
from datetime import datetime
from typing import Any, Dict, Optional

from sqlalchemy import DateTime, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class AuditLog(Base):
    """
    Immutable audit trail for all security-sensitive operations.

    AuditLog intentionally does NOT include TimestampMixin's updated_at
    because audit records must never be updated after creation.
    """

    __tablename__ = "audit_logs"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    # When the event occurred
    event_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False, index=True
    )

    # Who performed the action
    actor_id: Mapped[Optional[str]] = mapped_column(String(100), index=True)
    actor_username: Mapped[Optional[str]] = mapped_column(String(100))
    actor_ip: Mapped[Optional[str]] = mapped_column(String(50))

    # What action was performed
    action: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    # e.g. USER | ROLE | ROLE_ASSIGNMENT | SOD | MIGRATION
    resource_type: Mapped[Optional[str]] = mapped_column(String(50), index=True)
    resource_id: Mapped[Optional[str]] = mapped_column(String(100), index=True)
    resource_name: Mapped[Optional[str]] = mapped_column(String(300))

    # Outcome
    status: Mapped[str] = mapped_column(String(20), default="SUCCESS")  # SUCCESS | FAILURE
    detail: Mapped[Optional[str]] = mapped_column(Text)

    # Environment / tenant
    environment: Mapped[Optional[str]] = mapped_column(String(50))
    tenant_id: Mapped[Optional[str]] = mapped_column(String(100))

    def __repr__(self) -> str:  # pragma: no cover
        return f"<AuditLog id={self.id} action={self.action} actor={self.actor_username}>"
