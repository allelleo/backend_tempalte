from fastapi import HTTPException
from starlette import status


class UsernameExistsException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail={
            "message": "Username exists."
        })


class EmailExistsException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail={
            "message": "Email exists."
        })


class UserNotFoundByEmailException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail={
            "message": "User not found by email."
        })


class WrongPasswordException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_403_FORBIDDEN, detail={
            "message": "Wrong password."
        })
