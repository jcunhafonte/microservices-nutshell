from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from modules.users.users_module import UsersModule
from modules.meta.meta_module import MetaModule


app = FastAPI(
    debug=True,
    title="Insights Service",
    description="Insights demo service to fetch permissions from permissions service",
    version="0.0.1",
)

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"https?://(.+\.)*localhost(:\d+)?",
    allow_methods=("*",),
    allow_headers=("*",),
    allow_credentials=True,
    max_age=3600,
)

app.include_router(MetaModule.router)
app.include_router(UsersModule.router)
