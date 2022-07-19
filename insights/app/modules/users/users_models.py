from tortoise.fields import IntField, CharField
from tortoise.models import Model


class User(Model):
    id: int = IntField(pk=True)
    username: str = CharField(255, unique=True)
