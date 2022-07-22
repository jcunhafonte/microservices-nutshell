from casbin.enforcer import Enforcer
from casbin_sqlalchemy_adapter import Adapter


adapter = Adapter("postgresql://permissions:permissions@permissions-database:5432/permissions")
enforcer = Enforcer("policies/ac_model.conf", adapter)
