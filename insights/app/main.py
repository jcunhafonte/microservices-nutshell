# from pathlib import Path

# import uvicorn
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from tortoise.contrib.fastapi import register_tortoise


# from casbin.config import settings
# from casbin.modules.meta.meta_module import MetaModule
# from casbin.modules.users.users_module import UsersModule


# app = FastAPI()



# #
# # register all middlewares & other stuff here
# #
# register_tortoise(app, settings.tortoise_orm_config)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origin_regex=r"https?://(.+\.)*localhost(:\d+)?",
#     allow_methods=("*",),
#     allow_headers=("*",),
#     allow_credentials=True,
#     max_age=3600,
# )


# #
# # register all routers here
# #
# app.include_router(MetaModule.router)
# app.include_router(UsersModule.router)


# if __name__ == "__main__":
#     uvicorn.run(
#         "casbin.server:app",
#         host="0.0.0.0",
#         reload=not settings.python_env.startswith("prod"),
#         reload_dirs=["casbin"],
#     )

import grpc
import permission_pb2
import permission_pb2_grpc


from typing import Union
from fastapi import FastAPI


app = FastAPI(
    debug=True,
    title="Insights Service",
    description="Insights demo service to fetch permissions from permissions service",
    version="0.0.1",
)

permissions_service = grpc.insecure_channel("permissions:50051")
stub = permission_pb2_grpc.PermissionStub(permissions_service)

from modules.users.users_module import UsersModule

app.include_router(UsersModule.router)

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/users/{user_id}/policies")
# def get_user_policies(user_id: int):
#     """
#         **Get user policies**
        
#         `:param user_id: user id`

#         `:return: list of policies`
#     """
#     policy_request = permission_pb2.GetPolicyRequest(user_id=user_id)
#     policies_reply = stub.GetPolicies(policy_request)
#     policies = [dict(object=policy.object, action=policy.action) for policy in policies_reply.policies]

#     return {"policies": policies}


# @app.get("/test")
# def test(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}