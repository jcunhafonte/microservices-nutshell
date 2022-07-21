from pydantic import BaseModel


from modules.visualizations.visualizations_types import Chart


class Visualization(BaseModel):
    id: int
    title: str
    chart: Chart


class Visualizations(BaseModel):
    visualizations: list[Visualization]