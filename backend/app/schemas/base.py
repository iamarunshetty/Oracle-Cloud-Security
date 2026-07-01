"""Shared schema base and helpers."""

from pydantic import BaseModel, ConfigDict


class OrmBase(BaseModel):
    """Base schema that enables ORM mode for all response schemas."""

    model_config = ConfigDict(from_attributes=True)
