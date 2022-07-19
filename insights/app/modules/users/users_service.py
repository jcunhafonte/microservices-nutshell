from fastapi import HTTPException
from jose import JWTError, jwt
from jose.constants import ALGORITHMS
from tortoise.queryset import QuerySet


from config import settings


from .users_models import UserModel


class UsersService:
    def _decode_access_token(self, token: str) -> str:
        try:
            payload = jwt.decode(
                token, settings.jwt_secret, algorithms=[ALGORITHMS.HS256]
            )
            sub = payload["sub"]
            return sub
        except (JWTError, KeyError):
            raise HTTPException(status_code=401)

    def read_users_queryset(self, *, filters: dict = {}) -> QuerySet[UserModel]:
        return UserModel.filter(**filters)

    async def read_user_by_access_token(self, token: str) -> UserModel:
        sub = self._decode_access_token(token)
        user = await UserModel.get(username=sub)
        return user

    async def read_user_by_id(self, id: int) -> UserModel:
        user = await UserModel.get(id=id)
        return user
