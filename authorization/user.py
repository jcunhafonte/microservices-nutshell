import grpc


from typing import List
from functools import wraps
from casbin.enforcer import Enforcer
from casbin.persist.adapters import FileAdapter


class User:
    def __init__(self, id: int):
        self.id = str(id)
        self.enforcer = Enforcer("authorization/casbinmodel.conf", FileAdapter('authorization/ac_policy.csv'))

    @staticmethod
    def get_all():
        return {1, 2}

    def get_policies(self) -> List[List]:
        return self.enforcer.get_filtered_policy(0, self.id)

    def add_policy(self, object: str, action: str):
        self.enforcer.add_named_policy("p", self.id, object, action)
        self.enforcer.save_policy()

    def has_policy(self, object: str, action:str):
        if self.enforcer.enforce(self.id, object, action):
            return dict(status_code=200, message=f"User {self.id} has access!")

        return dict(status_code=401, message=f"User {self.id} is not authorized")

        


def validate_user(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if args[1].user_id not in User.get_all():
            raise grpc.RpcError(grpc.StatusCode.NOT_FOUND, 'User not found')
        return func(*args, **kwargs)
    return wrapper