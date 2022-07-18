from casbin.enforcer import Enforcer
from casbin.persist.adapters import FileAdapter


class Casbin():
    """
    Casbin class that receives the location of the casbinmodel or it loads the default one
    """

    def __init__(self, model: str = "authorization/casbinmodel.conf"):
        self.enforcer = Enforcer(model, FileAdapter('authorization/ac_policy.csv'))

    
    def get_users():
        return {1, 2} 


        