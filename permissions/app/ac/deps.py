from casbin_sqlalchemy_adapter import Adapter
from casbin.enforcer import Enforcer
from casbin.persist.adapters import FileAdapter



adapter = Adapter('postgresql://permission-user:database@permissions-database:5433/permission')

enforcer = Enforcer("ac/ac_model.conf", adapter)
