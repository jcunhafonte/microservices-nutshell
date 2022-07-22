from os import getenv

from casbin.enforcer import Enforcer
from casbin_sqlalchemy_adapter import Adapter


host, port, user, password, dbname = getenv("DATABASE_HOST"), getenv("POSTGRES_PORT"), getenv("POSTGRES_USER"), getenv("POSTGRES_PASSWORD"), getenv("POSTGRES_DB")
adapter = Adapter(f"postgresql://{user}:{password}@{host}:{port}/{dbname}")
enforcer = Enforcer("policies/ac_model.conf", adapter)
