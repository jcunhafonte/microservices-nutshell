from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str


class Users(BaseModel):
    users: list[User]