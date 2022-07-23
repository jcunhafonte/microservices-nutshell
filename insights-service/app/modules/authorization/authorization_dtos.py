from pydantic import BaseModel


class Authorization(BaseModel):
    id: int | None = None
