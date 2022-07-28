from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from modules.health.health_module import HealthModule
from modules.token.token_module import TokenModule


app = FastAPI(
    debug=True,
    title="Authentication Service",
    description="Authentication demo service to fetch permissions from permissions service.",
    version="0.0.1",
    root_path="/authentication"
)

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"https?://(.+\.)*localhost(:\d+)?",
    allow_methods=("*",),
    allow_headers=("*",),
    allow_credentials=True,
    max_age=3600,
)

app.include_router(HealthModule.router)
app.include_router(TokenModule.router)
