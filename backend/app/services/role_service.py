"""Role service — business logic for role management."""

from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.role import Role
from app.repositories.role_repository import RoleRepository
from app.schemas.role import RoleCreate, RoleUpdate


class RoleService:
    def __init__(self, db: Session) -> None:
        self.repo = RoleRepository(db)

    def get_role(self, role_id: str) -> Optional[Role]:
        return self.repo.get(role_id)

    def get_role_by_code(self, role_code: str) -> Optional[Role]:
        return self.repo.get_by_code(role_code)

    def list_roles(self, skip: int = 0, limit: int = 100) -> List[Role]:
        return self.repo.list(skip=skip, limit=limit)

    def search_roles(self, query: str, skip: int = 0, limit: int = 100) -> List[Role]:
        return self.repo.search(query, skip=skip, limit=limit)

    def create_role(self, data: RoleCreate) -> Role:
        role = Role(**data.model_dump(exclude_none=True))
        return self.repo.create(role)

    def update_role(self, role_id: str, data: RoleUpdate) -> Optional[Role]:
        role = self.repo.get(role_id)
        if not role:
            return None
        for field, value in data.model_dump(exclude_none=True).items():
            setattr(role, field, value)
        return self.repo.update(role)

    def delete_role(self, role_id: str) -> bool:
        role = self.repo.get(role_id)
        if not role:
            return False
        self.repo.delete(role)
        return True
