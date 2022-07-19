from .users_dtos import User
from .users_models import UserModel


class UsersMapper:
    def to_user_read(self, user: UserModel) -> User:
        return User(
            id=user.id,
            name=user.role,
            email=user.email,
        )
