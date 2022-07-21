from fastapi import Depends, HTTPException


from modules.users.users_models import UserModel
from modules.users.users_deps import get_current_user
from modules.policies.policies_service import PoliciesService


class GetAuthorizedUser:
    policies_service = PoliciesService()

    def __init__(self, resource: str, permission: str):
        self.resource = resource
        self.permission = permission

    def __call__(self, me: UserModel = Depends(get_current_user)):
        check_policy = self.policies_service.get_check_policy_by_user_id(me.id, self.resource, self.permission)
        
        if not check_policy.access:
            raise HTTPException(status_code=403)

        return me

get_authorized_user = lambda resource, permission: GetAuthorizedUser(resource, permission)