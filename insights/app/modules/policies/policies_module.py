from fastapi_module import module


from .policies_controller import PoliciesController


@module("/policies", controllers=(PoliciesController,))
class PoliciesModule:
    ...
