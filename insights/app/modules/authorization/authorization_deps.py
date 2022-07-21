from os import path

from fastapi import Depends, HTTPException, Request


from modules.users.users_deps import get_current_user
from modules.users.users_models import UserModel


def get_authorized_user(request: Request, me: UserModel = Depends(get_current_user)) -> UserModel:
    return me

    # sub = me.role
    # obj = req.url.path.removeprefix(settings.root_path)
    # act = req.method

    # if enforcer.enforce(sub, obj, act):
    #     return me

    raise HTTPException(status_code=403)
