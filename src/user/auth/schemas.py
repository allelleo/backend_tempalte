from pydantic import BaseModel, EmailStr


class SignUpRequest(BaseModel):
    email: EmailStr
    username: str
    first_name: str
    last_name: str
    password: str

class SignInRequest(BaseModel):
    email: EmailStr
    password: str