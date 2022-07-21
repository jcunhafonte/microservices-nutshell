from fastapi import Depends
from fastapi_module import InferringRouter, controller


from modules.authorization.authorization_deps import get_authorized_user
from modules.users.users_dtos import User
from modules.policies.policies_service import PoliciesService
from modules.policies.policies_mapper import PoliciesMapper
from modules.policies.policies_dtos import Policy, Policies


router = InferringRouter(tags=["Policies"])


@controller(router, version=1.1)
class PoliciesController:
    policies_service: PoliciesService = Depends()
    policies_mapper: PoliciesMapper = Depends()

    @router.get("/")
    async def get_policies(self, me: User = Depends(get_authorized_user("policies", "read"))) -> Policies:
        """
        **Create policy**

        Requires: `admin`

        `:return: list of users`
        """
        return None

    @router.post("/")
    async def create_policy(self, policy: Policy, me: User = Depends(get_authorized_user)) -> Policy:
        """
        **Create policy**

        Requires: `admin`

        `:return: list of users`
        """
        policy = self.policies_service.create_policy()
        return None
       # return self.users_mapper.to_users(users)
