from typing import List
from fastapi import HTTPException


from modules.users.users_models import UserModel


class UsersService:
    SECRET = "SECRET"
    ALGORITHM = "HS256"

    def get_users(self) -> List[UserModel]:
        return UserModel.all()

    def get_user_by_id(self, id: int) -> UserModel | HTTPException:
        user = UserModel.get(id=id)

        if user is None:
            raise HTTPException(status_code=404)

        return user
