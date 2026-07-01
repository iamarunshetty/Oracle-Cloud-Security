"""Role ORM model."""

import uuid
from typing import List, Optional

from sqlalchemy import Boolean, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.mixins import TimestampMixin


class Role(TimestampMixin, Base):
    """Represents an Oracle Fusion Cloud role (job role / duty role / abstract role)."""

    __tablename__ = "roles"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    # Oracle Fusion internal code (e.g. ORA_PER_LINE_MANAGER)
    role_code: Mapped[str] = mapped_column(String(200), unique=True, nullable=False, index=True)
    role_name: Mapped[str] = mapped_column(String(300), nullable=False)
    role_type: Mapped[Optional[str]] = mapped_column(
        String(50)
    )  # JOB_ROLE | DUTY_ROLE | ABSTRACT_ROLE | DATA_ROLE
    category: Mapped[Optional[str]] = mapped_column(String(100))
    description: Mapped[Optional[str]] = mapped_column(Text)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    # Relationships
    user_assignments: Mapped[List["UserRoleAssignment"]] = relationship(
        back_populates="role", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:  # pragma: no cover
        return f"<Role id={self.id} code={self.role_code}>"
