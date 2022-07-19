from types import ModuleType


from pydantic import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = ".env"

    python_env: str = "dev"
    root_path: str = ""

    database_uri: str = "asfas"
    redis_dsn: str = "fasfa"

    jwt_secret: str = "asf"
    jwt_exp_seconds: int = -1  # no EXP

    @property
    def tortoise_orm_model_modules(self) -> tuple[ModuleType, ...]:
        from modules.users import users_models

        return (users_models, )

    @property
    def tortoise_orm_config(self) -> dict:
        return {
            "connections": {
                "default": self.database_uri,
            },
            "apps": {
                "default": {
                    "models": self.tortoise_orm_model_modules,
                }
            },
            "use_tz": True,
        }

    @property
    def token_url(self) -> str:
        return f"{self.root_path}/v1/users/sign-in"


settings = Settings()
tortoise_orm_config = settings.tortoise_orm_config
