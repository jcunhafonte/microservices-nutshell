from datetime import datetime, timedelta, timezone
from typing import Any

from fastapi import HTTPException
from jose import JWTError, jwt
from jose.constants import ALGORITHMS
from passlib.context import CryptContext
from tortoise.queryset import QuerySet

from config import settings

from .users_models import User
from .users_types import Role


class UsersService:
    crypt_ctx = CryptContext(schemes=["bcrypt"])

    def _hash_password(self, password: str) -> str:
        return self.crypt_ctx.hash(password)

    def _verify_password(self, password: str, password_hash: str) -> bool:
        return self.crypt_ctx.verify(password, password_hash)

    def _encode_access_token(self, sub: str) -> str:
        payload: dict[str, Any] = {"sub": sub}
        exp = settings.jwt_exp_seconds
        if exp > 0:
            payload["exp"] = datetime.now(timezone.utc) + timedelta(seconds=exp)
        access_token = jwt.encode(
            payload, settings.jwt_secret, algorithm=ALGORITHMS.HS256
        )
        return access_token

    def _decode_access_token(self, token: str) -> str:
        try:
            payload = jwt.decode(
                token, settings.jwt_secret, algorithms=[ALGORITHMS.HS256]
            )
            sub = payload["sub"]
            return sub
        except (JWTError, KeyError):
            raise HTTPException(status_code=401)

    def read_users_queryset(self, *, filters: dict = {}) -> QuerySet[User]:
        return User.filter(**filters)

    async def read_user_by_access_token(self, token: str) -> User:
        sub = self._decode_access_token(token)
        user = await User.get(username=sub)
        return user

    async def read_user_by_id(self, id: int) -> User:
        user = await User.get(id=id)
        return user
