from tortoise.fields import (
    BooleanField,
    CharField,
    DatetimeField,
    IntField,
)
from tortoise.models import Model
from user.security import get_hashed_password, verify_password


class User(Model):
    """Модель базы данных для пользователя"""
    id = IntField(pk=True)
    time_created = DatetimeField(auto_now_add=True)
    time_updated = DatetimeField(auto_now=True)

    email = CharField(max_length=30, unique=True)

    username = CharField(max_length=30, unique=True)
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)
    password = CharField(max_length=100)

    is_admin = BooleanField(default=False)

    async def set_password(self, password: str):
        self.password = await get_hashed_password(password=password)

    async def check_password(self, password):
        return await verify_password(password, self.password)
