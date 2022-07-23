from fastapi import Request
from fastapi_module import InferringRouter, controller


router = InferringRouter(tags=["Health"])


@controller(router, version=1.1)
class HealthController:
    @router.get("/")
    def health(self, req: Request) -> dict:
        return {
            "healthy": True,
        }
