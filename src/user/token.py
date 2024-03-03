import jwt
import datetime
from core.settings import ALGORITHM, JWT_SECRET_KEY, TOKEN_EXPIRE
from user.exceptions import InvalidTokenException


async def create_token(payload: dict) -> str:
    return jwt.encode(payload, JWT_SECRET_KEY, ALGORITHM)


async def decode_token(token: str) -> dict:
    try:
        return jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
    except Exception as e:
        print(str(e))
        raise InvalidTokenException
