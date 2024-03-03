from fastapi import HTTPException
from starlette import status


class InvalidTokenException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail={
            "message": "Token is invalid."
        })


class UnAuthorizedException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail={
            "message": "User un authorized."
        })
