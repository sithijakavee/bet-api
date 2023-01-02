from pydantic import BaseModel


class Register(BaseModel):
    username: str
    email: str
    password: str
    phoneNumber: str

class Login(BaseModel):
    email: str
    password: str

class User(BaseModel):
    id: str

class Bet(BaseModel):
    userid : str
    username : str
    bet_amount : str
    bet_event : str
    bet_sport : str
    bets : str