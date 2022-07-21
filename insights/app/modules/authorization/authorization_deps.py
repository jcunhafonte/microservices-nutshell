from fastapi import Depends, HTTPException


from modules.users.users_deps import get_current_user
from modules.users.users_models import UserModel


class GetAuthorizedUser:
    def __init__(self, resource: str, permission: str):
        self.resource = resource
        self.permission = permission

    def __call__(self, me: UserModel = Depends(get_current_user)):
        print(me)
        print(self.resource)
        print(self.permission)

        # Call policiy service to check if user has permission
        # if not:
        #     raise HTTPException(status_code=403)
        return me

        raise HTTPException(status_code=403)


get_authorized_user = lambda resource, permission: GetAuthorizedUser(resource, permission)


    # sub = me.role
    # obj = req.url.path.removeprefix(settings.root_path)
    # act = req.method

    # if enforcer.enforce(sub, obj, act):
    #     return me

 #   raise HTTPException(status_code=403)
