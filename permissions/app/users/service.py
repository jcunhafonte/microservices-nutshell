from typing import List


from users.users_models import UserModel


class UsersService:
    def get_users(self) -> List[UserModel]:
        return UserModel.all()
