from fastapi import Depends
from fastapi_module import InferringRouter, controller


from modules.authorization.authorization_deps import get_authorized_user
from modules.visualizations.visualizations_dtos import Visualization, Visualizations
from modules.visualizations.visualizations_mapper import VisualizationsMapper
from modules.visualizations.visualizations_service import VisualizationsService
from modules.users.users_dtos import User


router = InferringRouter(tags=["Visualizations"])


@controller(router, version=1.1)
class VisualizationsController:
    visualizations_service: VisualizationsService = Depends()
    visualizations_mapper: VisualizationsMapper = Depends()

    @router.get("/")
    async def get_visualizations(self, me: User = Depends(get_authorized_user("visualizations", "read"))) -> Visualizations:
        """
        **Get visualizations**

        `:return: list of visualizations`
        """
        visualizations = self.visualizations_service.get_visualizations()
        return self.visualizations_mapper.to_visualizations(visualizations)

    @router.get("/{visualization_id}")
    async def get_visualization(self, visualization_id: int, me: User = Depends(get_authorized_user("visualizations", "read"))) -> Visualization:
        """
        **Get visualization**

        `:param visualization_id: visualization id`

        `:return: visualization`
        """
        visualization = self.visualizations_service.get_visualization_by_id(visualization_id)
        return self.visualizations_mapper.to_visualization(visualization)
