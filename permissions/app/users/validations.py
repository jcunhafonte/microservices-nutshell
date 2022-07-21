import grpc
from functools import wraps


from users.service import UsersService


def validate_user(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if args[1].user_id not in UsersService().get_users():
            raise grpc.RpcError(grpc.StatusCode.NOT_FOUND, "User not found")
        return func(*args, **kwargs)
    return wrapper 