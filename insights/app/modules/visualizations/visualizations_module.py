from fastapi_module import module


from modules.visualizations.visualizations_controller import VisualizationsController


@module("/visualizations", controllers=(VisualizationsController,))
class VisualizationsModule:
    ...
