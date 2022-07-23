from modules.visualizations.visualizations_types import Chart


class VisualizationModel:
    visualizations = {
        1: dict(
            id=1,
            title="Visualization 1",
            chart=Chart.bar,
        ),
        2: dict(
            id=2,
            title="Visualization 2",
            chart=Chart.line,
        ),
        3: dict(
            id=3,
            title="Visualization 3",
            chart=Chart.pie,
        ),
        4: dict(
            id=4,
            title="Visualization 4",
            chart=Chart.bar,
        ),
        5: dict(
            id=5,
            title="Visualization 5",
            chart=Chart.pie,
        ),
    }

    def __init__(self, id: int, title: str, chart: Chart):
        self.id = id
        self.title = title
        self.chart = chart

    @staticmethod
    def all() -> list:
        return [VisualizationModel(**visualization) for visualization in list(VisualizationModel.visualizations.values())]

    @staticmethod
    def get(id: int) -> dict | None:
        if id in VisualizationModel.visualizations:
            return VisualizationModel(**VisualizationModel.visualizations[id])

        return None
