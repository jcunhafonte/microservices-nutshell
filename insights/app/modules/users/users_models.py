from http.client import HTTPException


class UserModel:
    users = {
        1: dict(
            id=1,
            name="Cloudbeds Admin",
            email="admin@cloudbeds.com",
        ),
         2: dict(
            id=2,
            name="Alice Wonderson",
            email="alice@example.com",
        )
    }

    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

    @staticmethod
    def get(id: int) -> dict:
        if id in UserModel.users:
            return UserModel(**UserModel.users[id])

        raise HTTPException(status_code=404)

    @staticmethod
    def all() -> list:
        return [UserModel(**user) for user in list(UserModel.users.values())]
