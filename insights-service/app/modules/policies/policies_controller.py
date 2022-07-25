from fastapi import Depends
from fastapi_module import InferringRouter, controller


from modules.authorization.authorization_deps import get_authorized_user
from modules.users.users_dtos import User
from modules.policies.policies_service import PoliciesService
from modules.policies.policies_mapper import PoliciesMapper
from modules.policies.policies_dtos import Policy, PolicyRequest, Policies


router = InferringRouter(tags=["Policies"])


@controller(router, version=1.1)
class PoliciesController:
    policies_service: PoliciesService = Depends()
    policies_mapper: PoliciesMapper = Depends()

    @router.get("/")
    async def get_policies(self, me: User = Depends(get_authorized_user("admin", "write"))) -> Policies:
        """
        **Get policies**

        Requires: `admin`

        `:return: policies`
        """
        policies = self.policies_service.get_policies().policies
        return self.policies_mapper.to_policies(policies)

    @router.post("/")
    async def create_policy(self, policy: PolicyRequest, me: User = Depends(get_authorized_user("admin", "write"))) -> Policy:
        """
        **Create policy**

        Requires: `admin`

        `:return: policy`
        """
        policy = self.policies_service.create_policy_by_user_id(policy.user_id, policy.object, policy.action)
        return self.policies_mapper.to_policy(policy)
