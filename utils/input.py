import grpc


def input_user_id() -> int:
    user_id = input("Please enter a user_id (or nothing to stop chatting): ")

    if user_id == '':
        raise grpc.RpcError(grpc.StatusCode.INVALID_ARGUMENT, 'User Id can not be null')

    return int(user_id)

def input_object() -> str:
    return input("Please enter a object for the policy (or nothing to stop chatting): ")

def input_action() -> str:
    return input("Please enter a action policy (or nothing to stop chatting): ")

def input_available_actions() -> str:
    return input("Do you want to get policies or create them?\n-(G)|(C)|(V): ")