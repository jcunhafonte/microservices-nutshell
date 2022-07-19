from fastapi import Request
from fastapi_module import InferringRouter, controller


router = InferringRouter(tags=["meta"])


@controller(router, version=1.1)
class MetaController:
    @router.get("/ping")
    def pong(self, req: Request) -> dict:
        return {
            "message": "PONG",
            "root_path": req.scope.get("root_path"),
        }
