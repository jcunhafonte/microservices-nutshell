from typing import List


from modules.visualizations.visualizations_models import VisualizationModel


class VisualizationsService:
    def get_visualizations(self) -> List[VisualizationModel]:
        return VisualizationModel.all()

    def get_visualization_by_id(self, id: int) -> VisualizationModel:
        visualization = VisualizationModel.get(id=id)
        return visualization
