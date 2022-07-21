from typing import List


from .users_dtos import User, Users
from .users_models import UserModel


class UsersMapper:
    def to_user(self, user: UserModel) -> User:
        return User(id=user.id, name=user.name, email=user.email)

    def to_users(self, users: List[UserModel]) -> Users:
        return Users(users=[self.to_user(user) for user in users])
