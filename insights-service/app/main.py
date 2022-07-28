from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from modules.health.health_module import HealthModule
from modules.users.users_module import UsersModule
from modules.policies.policies_module import PoliciesModule
from modules.reports.reports_module import ReportsModule
from modules.visualizations.visualizations_module import VisualizationsModule


app = FastAPI(
    debug=True,
    title="Insights Service",
    description="Insights demo service to fetch permissions from permissions service.",
    version="0.0.1",
    root_path="/insights"
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
app.include_router(UsersModule.router)
app.include_router(ReportsModule.router)
app.include_router(VisualizationsModule.router)
app.include_router(PoliciesModule.router)
