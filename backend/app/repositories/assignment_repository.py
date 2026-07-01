"""UserRoleAssignment repository."""

from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.user_role_assignment import UserRoleAssignment
from app.repositories.base import BaseRepository


class AssignmentRepository(BaseRepository[UserRoleAssignment]):
    def __init__(self, db: Session) -> None:
        super().__init__(UserRoleAssignment, db)

    def get_by_user(self, user_id: str) -> List[UserRoleAssignment]:
        return (
            self.db.query(UserRoleAssignment)
            .filter(
                UserRoleAssignment.user_id == user_id,
                UserRoleAssignment.removed_at.is_(None),
            )
            .all()
        )

    def get_active_assignment(
        self, user_id: str, role_id: str
    ) -> Optional[UserRoleAssignment]:
        return (
            self.db.query(UserRoleAssignment)
            .filter(
                UserRoleAssignment.user_id == user_id,
                UserRoleAssignment.role_id == role_id,
                UserRoleAssignment.removed_at.is_(None),
            )
            .first()
        )
