from fastapi import Depends
from fastapi.security import HTTPBearer


from .users_service import UsersService
from .users_models import UserModel


BEARER_FORMAT = "JWT"
SCHEME_NAME = "Authorization"
DESCRIPTION = """
**Admin** eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwibmFtZSI6IkFkbWluIENsb3VkYmVkcyIsImVtYWlsIjoiYWRtaW5AY2xvdWRiZWRzLmNvbSIsImlhdCI6MTUxNjIzOTAyMn0.28UzNl63W_6cDXM4Z95G4TaEV-JsgzftDfCSpYjANuc

**User** eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyIiwibmFtZSI6IkFsaWNlIFdvbmRlcnNvbiIsImVtYWlsIjoiYWxpY2VAZXhhbXBsZS5jb20iLCJpYXQiOjE1MTYyMzkwMjJ9.XIym2MZVF1RcT0GzbpxqQmUvDSSYmRzKAfv84p4JBr0
"""

async def get_current_user(
    users_service: UsersService = Depends(),
    token: str = Depends(HTTPBearer(bearerFormat=BEARER_FORMAT, scheme_name=SCHEME_NAME, description=DESCRIPTION))
) -> UserModel:
    me = users_service.get_user_by_access_token(token.credentials)
    return me
