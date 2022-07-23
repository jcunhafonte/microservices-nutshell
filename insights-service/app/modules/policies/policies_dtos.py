from pydantic import BaseModel


class Policy(BaseModel):
    object: str
    action: str

class PolicyRequest(Policy):
    user_id: int

class Policies(BaseModel):
    policies: list[Policy]