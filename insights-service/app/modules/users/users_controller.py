from fastapi import Depends, Request
from fastapi_module import InferringRouter, controller


from modules.authorization.authorization_deps import get_authorized_user
from modules.users.users_dtos import User, Users
from modules.users.users_mapper import UsersMapper
from modules.users.users_service import UsersService
from modules.users.users_deps import get_current_user
from modules.policies.policies_service import PoliciesService
from modules.policies.policies_mapper import PoliciesMapper
from modules.policies.policies_dtos import Policies


router = InferringRouter(tags=["Users"])


@controller(router, version=1.1)
class UsersController:
    users_service: UsersService = Depends()
    users_mapper: UsersMapper = Depends()
    policies_service: PoliciesService = Depends()
    policies_mapper: PoliciesMapper = Depends()

    @router.get("/")
    async def get_users(self, me: User = Depends(get_authorized_user("admin", "read"))) -> Users:
        """
        **Get users**

        Requires: `admin`

        `:return: list of users`
        """
        users = self.users_service.get_users()
        return self.users_mapper.to_users(users)

    @router.get("/me")
    async def get_me(self, request: Request, me: User = Depends(get_current_user)) -> User:
        """
        **Get me**

        `:return: user`
        """
        print(request.headers)
        return self.users_mapper.to_user(me)

    @router.get("/me/policies")
    async def get_me_policies(self, me: User = Depends(get_current_user)) -> Policies:
        """
        **Get my policies**

        `:return: user`
        """
        policies = self.policies_service.get_policies_by_user_id(me.id).policies
        return self.policies_mapper.to_policies(policies)

    @router.get("/{user_id}")
    async def get_user(self, user_id: int, me: User = Depends(get_authorized_user("admin", "read"))) -> User:
        """
        **Get user**

        Requires: `admin`

        `:param user_id: user id`

        `:return: user`
        """
        user = self.users_service.get_user_by_id(user_id)
        return self.users_mapper.to_user(user)

    @router.get("/{user_id}/policies")
    async def get_user_policies(self, user_id: int, me: User = Depends(get_authorized_user("admin", "read"))) -> Policies:
        """
        **Get user policies**

        Requires: `admin`

        `:param user_id: user id`

        `:return: list of policies`
        """
        policies = self.policies_service.get_policies_by_user_id(user_id).policies
        return self.policies_mapper.to_policies(policies)
