from pydantic import BaseModel


class Report(BaseModel):
    id: int
    title: str
    description: str


class Reports(BaseModel):
    reports: list[Report]