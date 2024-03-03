from fastapi import APIRouter, Depends, Request
from user.auth import schemas, service

auth = APIRouter()


@auth.post('/sign-in')
async def sign_in(data: schemas.SignInRequest):
    return await service.sign_in(data)


@auth.post('/sign-up')
async def sign_up(data: schemas.SignUpRequest):
    return await service.sign_up(data)
