from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer


from modules.token.token_service import TokenService
from modules.token.token_models import TokenModel
from common.constants import BEARER_FORMAT, SCHEME_NAME, ADMIN_TOKEN, USER_TOKEN


DESCRIPTION = f"""
**Admin** {ADMIN_TOKEN}

**User** {USER_TOKEN}
"""

async def get_current_token(
    token_service: TokenService = Depends(),
    token: str = Depends(HTTPBearer(bearerFormat=BEARER_FORMAT, scheme_name=SCHEME_NAME, description=DESCRIPTION, auto_error=False))
) -> TokenModel:
    if token is None:
        raise HTTPException(status_code=401, detail="Not authenticated")
   
    token = token_service.get_token(token.credentials)
    return token
