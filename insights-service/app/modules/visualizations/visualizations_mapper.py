from typing import List


from modules.visualizations.visualizations_dtos import Visualization, Visualizations
from modules.visualizations.visualizations_models import VisualizationModel


class VisualizationsMapper:
    def to_visualization(self, visualization: VisualizationModel) -> Visualization:
        return Visualization(id=1, title=visualization.title, chart=visualization.chart)

    def to_visualizations(self, visualizations: List[VisualizationModel]) -> Visualizations:
        return Visualizations(visualizations=[self.to_visualization(visualization) for visualization in visualizations])
