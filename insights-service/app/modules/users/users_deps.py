from fastapi import Depends, HTTPException, Request
from fastapi.security import HTTPBearer


from modules.users.users_service import UsersService
from modules.users.users_models import UserModel
from common.constants import BEARER_FORMAT, SCHEME_NAME, ADMIN_TOKEN, USER_TOKEN


DESCRIPTION = f"""
**Admin** {ADMIN_TOKEN}

**User** {USER_TOKEN}
"""

async def get_current_user(
    request: Request,
    users_service: UsersService = Depends(),
    token: str = Depends(HTTPBearer(bearerFormat=BEARER_FORMAT, scheme_name=SCHEME_NAME, description=DESCRIPTION, auto_error=False))
) -> UserModel:
    if token is None:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    user_id = int(request.headers.get('x-user-id'))
    me = users_service.get_user_by_id(user_id)
    return me
