from casbin.enforcer import Enforcer
from casbin.persist.adapters import FileAdapter


enforcer = Enforcer("ac/ac_model.conf", FileAdapter("ac/ac_policy.csv"))
