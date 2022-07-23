from fastapi_module import module


from modules.health.health_controller import HealthController


@module("/health", controllers=(HealthController,))
class HealthModule:
    ...
