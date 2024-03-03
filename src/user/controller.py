from fastapi import APIRouter, Depends, Request
from user.auth.controller import auth
from user import depends

user = APIRouter()
user.include_router(auth, prefix='/auth', tags=['auth'])


@user.get('/protected')
async def protected(usr: str = Depends(depends.get_user)):
    return usr
