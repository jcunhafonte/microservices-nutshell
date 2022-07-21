from pydantic import BaseModel


class Policy(BaseModel):
    object: str
    action: str


class Policies(BaseModel):
    policies: list[Policy]