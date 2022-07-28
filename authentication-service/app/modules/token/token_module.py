from fastapi_module import module


from modules.token.token_controller import TokenController


@module("/token", controllers=(TokenController,))
class TokenModule:
    ...
