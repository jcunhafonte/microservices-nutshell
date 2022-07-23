from fastapi_module import module


from modules.policies.policies_controller import PoliciesController


@module("/policies", controllers=(PoliciesController,))
class PoliciesModule:
    ...
