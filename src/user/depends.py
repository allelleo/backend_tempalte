from fastapi import Header, Depends
from user import exceptions, token, models


async def authorization_header(authorization: str = Header(None)):
    if authorization is None:
        raise exceptions.UnAuthorizedException

    return authorization.split("Token")[-1].strip()


async def decode_token(jwt: str = Depends(authorization_header)):
    return await token.decode_token(jwt)


async def get_user(payload: dict = Depends(decode_token)):
    user_id = payload.get('user_id', None)

    if user_id is None:
        raise exceptions.InvalidTokenException

    if not await models.User.exists(id=user_id):
        raise exceptions.InvalidTokenException

    user = await models.User.get(id=user_id)
    return user
