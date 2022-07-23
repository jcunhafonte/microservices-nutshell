class UserModel:
    users = { 1, 2 }

    def __init__(self, id: int):
          self.id = id

    @staticmethod
    def all():
        return {1, 2}
