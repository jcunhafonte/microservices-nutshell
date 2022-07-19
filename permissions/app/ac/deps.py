from casbin.enforcer import Enforcer
from casbin.persist.adapters import FileAdapter


enforcer = Enforcer("app/ac/ac_model.conf", FileAdapter("app/ac/ac_policy.csv"))
