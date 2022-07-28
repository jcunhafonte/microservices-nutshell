from fastapi import HTTPException
from jose import JWTError, jwt
from jose.constants import ALGORITHMS


from modules.token.token_models import TokenModel


class TokenService:
    SECRET = "SECRET"
    ALGORITHM = "HS256"

    def __decode_access_token(self, token: str) -> str:
        try:
            payload = jwt.decode(token, self.SECRET, algorithms=[ALGORITHMS.HS256])
            return payload
        except (JWTError, KeyError):
            raise HTTPException(status_code=401)

    def get_token(self, token: str) -> TokenModel | HTTPException:
        token = self.__decode_access_token(token)
        token = TokenModel(**token)
        return token
