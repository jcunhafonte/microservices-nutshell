from typing import Optional


from .users_types import Role


from datetime import datetime

from pydantic import BaseModel
from tortoise.fields import DatetimeField, IntField
from tortoise.models import Model


class TortoiseModel(Model):
    class Meta:
        abstract = True

    id: int = IntField(pk=True)
    created_at: datetime = DatetimeField(auto_now_add=True)
    updated_at: datetime = DatetimeField(auto_now=True)


class PydanticModel(BaseModel):
    class Config:
        orm_mode = True


class UserRead(PydanticModel):
    id: int
    username: str
    role: Role


class UserUpdate(PydanticModel):
    role: Optional[Role] = None
