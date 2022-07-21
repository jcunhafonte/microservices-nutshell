from casbin.enforcer import Enforcer
from casbin.persist.adapters import FileAdapter


enforcer = Enforcer("policies/ac_model.conf", FileAdapter("policies/ac_policy.csv"))
