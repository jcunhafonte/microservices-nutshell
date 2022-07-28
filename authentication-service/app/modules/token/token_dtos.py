from pydantic import BaseModel


class TokenInfo(BaseModel):
    sub: str
    name: str
    email: str


class TokenVerify(BaseModel):
    valid: bool
