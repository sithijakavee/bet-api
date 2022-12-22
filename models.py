from pydantic import BaseModel


class Register(BaseModel):
    username: str
    email: str
    password: str
    phoneNumber: str

class Login(BaseModel):
    email: str
    password: str