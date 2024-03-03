from user import models, token
from user.auth import schemas, exceptions
from tortoise.transactions import in_transaction


async def sign_up(data: schemas.SignUpRequest):
    if await models.User.exists(email=data.email):
        raise exceptions.EmailExistsException
    if await models.User.exists(username=data.username):
        raise exceptions.UsernameExistsException

    async with in_transaction() as transaction:
        user = models.User(
            email=data.email,
            username=data.username,
            first_name=data.first_name,
            last_name=data.last_name,
        )
        await user.set_password(data.password)
        await user.save(using_db=transaction)

    return {"satus": "ok", "user_id": user.id}


async def sign_in(data: schemas.SignInRequest):
    if not await models.User.exists(email=data.email):
        raise exceptions.UserNotFoundByEmailException

    user = await models.User.get(email=data.email)

    if await user.check_password(data.password):
        return {"token": await token.create_token({"user_id": user.id})}
    raise exceptions.WrongPasswordException
