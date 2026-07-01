"""User repository."""

from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.base import BaseRepository


class UserRepository(BaseRepository[User]):
    def __init__(self, db: Session) -> None:
        super().__init__(User, db)

    def get_by_username(self, username: str) -> Optional[User]:
        return self.db.query(User).filter(User.username == username).first()

    def get_by_email(self, email: str) -> Optional[User]:
        return self.db.query(User).filter(User.email == email).first()

    def get_by_fusion_id(self, fusion_user_id: str) -> Optional[User]:
        return self.db.query(User).filter(User.fusion_user_id == fusion_user_id).first()

    def search(self, query: str, skip: int = 0, limit: int = 100) -> List[User]:
        pattern = f"%{query}%"
        return (
            self.db.query(User)
            .filter(
                User.username.ilike(pattern)
                | User.email.ilike(pattern)
                | User.first_name.ilike(pattern)
                | User.last_name.ilike(pattern)
            )
            .offset(skip)
            .limit(limit)
            .all()
        )
