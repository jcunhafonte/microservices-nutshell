from typing import List
from fastapi import HTTPException
from jose import JWTError, jwt
from jose.constants import ALGORITHMS


from .users_models import UserModel


class UsersService:
    SECRET = "SECRET"
    ALGORITHM = "HS256"

    def __decode_access_token(self, token: str) -> str:
        try:
            payload = jwt.decode(token, self.SECRET, algorithms=[ALGORITHMS.HS256])
            sub = payload["sub"]
            return sub
        except (JWTError, KeyError):
            raise HTTPException(status_code=401)

    def get_users(self) -> List[UserModel]:
        return UserModel.all()

    def get_user_by_access_token(self, token: str) -> UserModel:
        sub = self.__decode_access_token(token)
        user = UserModel.get(id=int(sub))
        return user

    def get_user_by_id(self, id: int) -> UserModel:
        user = UserModel.get(id=id)
        return user
