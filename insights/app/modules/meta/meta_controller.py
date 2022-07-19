from araneae.config import settings
from araneae.modules.ac.ac_deps import get_authorized_user
from araneae.modules.users.users_models import User
from fastapi import Depends, Request
from fastapi_module import InferringRouter, controller

router = InferringRouter(tags=["meta"])


@controller(router, version=1)
class MetaController:
    @router.get("/ping")
    def pong(self, req: Request) -> dict:
        return {
            "message": "PONG",
            "environment": settings.python_env,
            "root_path": req.scope.get("root_path"),
        }

    @router.get("/config")
    def read_config(self, me: User = Depends(get_authorized_user)) -> dict:
        return settings.dict()
