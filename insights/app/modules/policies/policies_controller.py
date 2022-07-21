from fastapi import Depends
from fastapi_module import InferringRouter, controller


from modules.authorization.authorization_deps import get_authorized_user
from modules.users.users_dtos import User
from modules.policies.policies_service import PoliciesService
from modules.policies.policies_mapper import PoliciesMapper
from modules.policies.policies_dtos import Policy, PolicyRequest


router = InferringRouter(tags=["Policies"])


@controller(router, version=1.1)
class PoliciesController:
    policies_service: PoliciesService = Depends()
    policies_mapper: PoliciesMapper = Depends()

    @router.post("/")
    async def create_policy(self, policy: PolicyRequest, me: User = Depends(get_authorized_user("policies", "write"))) -> Policy:
        """
        **Create policy**

        Requires: `admin`

        `:return: policy`
        """
        policy = self.policies_service.create_policy_by_user_id(policy.user_id, policy.object, policy.action)
        return self.policies_mapper.to_policy(policy)
