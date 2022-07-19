from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_module import InferringRouter, controller

from modules.ac.ac_deps import get_authorized_user


from .users_dtos import UserRead
from .users_mapper import UsersMapper
from .users_models import User
from .users_service import UsersService

router = InferringRouter(tags=["users"])


@controller(router, version=1)
class UsersController:
    users_service: UsersService = Depends()
    users_mapper: UsersMapper = Depends()

    @router.get("/")
    async def read_users(
        self,
        me: User = Depends(get_authorized_user),
    ) -> UserRead:
        qs = self.users_service.read_users_queryset()
        return []

    @router.get("/{user_id}")
    async def read_user(
        self,
        user_id: int,
        me: User = Depends(get_authorized_user),
    ) -> UserRead:
        user = await self.users_service.read_user_by_id(user_id)
        return self.users_mapper.to_user_read(user)