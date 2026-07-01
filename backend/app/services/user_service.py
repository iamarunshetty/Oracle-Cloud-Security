"""User service — business logic for user lifecycle management."""

from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserUpdate


class UserService:
    def __init__(self, db: Session) -> None:
        self.repo = UserRepository(db)

    def get_user(self, user_id: str) -> Optional[User]:
        return self.repo.get(user_id)

    def get_user_by_username(self, username: str) -> Optional[User]:
        return self.repo.get_by_username(username)

    def list_users(self, skip: int = 0, limit: int = 100) -> List[User]:
        return self.repo.list(skip=skip, limit=limit)

    def search_users(self, query: str, skip: int = 0, limit: int = 100) -> List[User]:
        return self.repo.search(query, skip=skip, limit=limit)

    def create_user(self, data: UserCreate) -> User:
        user = User(**data.model_dump(exclude_none=True))
        return self.repo.create(user)

    def update_user(self, user_id: str, data: UserUpdate) -> Optional[User]:
        user = self.repo.get(user_id)
        if not user:
            return None
        for field, value in data.model_dump(exclude_none=True).items():
            setattr(user, field, value)
        return self.repo.update(user)

    def lock_user(self, user_id: str) -> Optional[User]:
        user = self.repo.get(user_id)
        if not user:
            return None
        user.is_locked = True
        return self.repo.update(user)

    def unlock_user(self, user_id: str) -> Optional[User]:
        user = self.repo.get(user_id)
        if not user:
            return None
        user.is_locked = False
        return self.repo.update(user)

    def suspend_user(self, user_id: str) -> Optional[User]:
        user = self.repo.get(user_id)
        if not user:
            return None
        user.is_suspended = True
        return self.repo.update(user)

    def delete_user(self, user_id: str) -> bool:
        user = self.repo.get(user_id)
        if not user:
            return False
        self.repo.delete(user)
        return True
