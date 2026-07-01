"""Role repository."""

from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.role import Role
from app.repositories.base import BaseRepository


class RoleRepository(BaseRepository[Role]):
    def __init__(self, db: Session) -> None:
        super().__init__(Role, db)

    def get_by_code(self, role_code: str) -> Optional[Role]:
        return self.db.query(Role).filter(Role.role_code == role_code).first()

    def list_active(self, skip: int = 0, limit: int = 100) -> List[Role]:
        return (
            self.db.query(Role)
            .filter(Role.is_active == True)  # noqa: E712
            .offset(skip)
            .limit(limit)
            .all()
        )

    def search(self, query: str, skip: int = 0, limit: int = 100) -> List[Role]:
        pattern = f"%{query}%"
        return (
            self.db.query(Role)
            .filter(Role.role_code.ilike(pattern) | Role.role_name.ilike(pattern))
            .offset(skip)
            .limit(limit)
            .all()
        )
