from fastapi_module import module


from modules.users.users_controller import UsersController


@module("/users", controllers=(UsersController,))
class UsersModule:
    ...
