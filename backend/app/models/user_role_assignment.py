"""UserRoleAssignment ORM model."""

import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.mixins import TimestampMixin


class UserRoleAssignment(TimestampMixin, Base):
    """Junction table linking users to roles with assignment metadata."""

    __tablename__ = "user_role_assignments"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    user_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    role_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("roles.id", ondelete="CASCADE"), nullable=False, index=True
    )

    # Assignment lifecycle
    assigned_by: Mapped[Optional[str]] = mapped_column(String(100))
    assigned_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))
    expires_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))
    removed_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))
    removed_by: Mapped[Optional[str]] = mapped_column(String(100))

    # Approval / workflow reference
    approval_request_id: Mapped[Optional[str]] = mapped_column(String(100))
    justification: Mapped[Optional[str]] = mapped_column(String(500))

    # Relationships
    user: Mapped["User"] = relationship(back_populates="role_assignments")
    role: Mapped["Role"] = relationship(back_populates="user_assignments")

    def __repr__(self) -> str:  # pragma: no cover
        return f"<UserRoleAssignment user={self.user_id} role={self.role_id}>"
