from fastapi import Depends


from .users_models import User
from .users_service import UsersService


async def get_current_user(
    users_service: UsersService = Depends(),
) -> User:
    # me = await users_service.read_user_by_access_token(token)
    return dict()
