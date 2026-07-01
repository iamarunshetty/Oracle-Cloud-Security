"""Assignment service — business logic for user-role assignment lifecycle."""

from datetime import datetime, timezone
from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.user_role_assignment import UserRoleAssignment
from app.repositories.assignment_repository import AssignmentRepository
from app.schemas.assignment import AssignRoleRequest


class AssignmentService:
    def __init__(self, db: Session) -> None:
        self.repo = AssignmentRepository(db)

    def assign_role(self, data: AssignRoleRequest) -> UserRoleAssignment:
        # Check for an existing active assignment to avoid duplicates
        existing = self.repo.get_active_assignment(data.user_id, data.role_id)
        if existing:
            return existing

        assignment = UserRoleAssignment(
            user_id=data.user_id,
            role_id=data.role_id,
            assigned_by=data.assigned_by,
            assigned_at=datetime.now(tz=timezone.utc),
            expires_at=data.expires_at,
            justification=data.justification,
        )
        return self.repo.create(assignment)

    def remove_role(
        self, user_id: str, role_id: str, removed_by: Optional[str] = None
    ) -> Optional[UserRoleAssignment]:
        assignment = self.repo.get_active_assignment(user_id, role_id)
        if not assignment:
            return None
        assignment.removed_at = datetime.now(tz=timezone.utc)
        assignment.removed_by = removed_by
        return self.repo.update(assignment)

    def list_user_assignments(self, user_id: str) -> List[UserRoleAssignment]:
        return self.repo.get_by_user(user_id)

    def get_assignment(self, assignment_id: str) -> Optional[UserRoleAssignment]:
        return self.repo.get(assignment_id)
