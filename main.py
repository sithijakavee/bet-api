
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import db
from functions import getUserById
import models
import uuid

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/register")
async def register(register: models.Register):

    cursor = db.cursor()

    sql = "SELECT * FROM users WHERE email = %s"
    val = (register.email,)
    cursor.execute(sql, val)

    result = cursor.fetchall()

    if result:
        return "Email already used! Please try again with different email"

    else:
        cursor = db.cursor()

        userid = uuid.uuid1()

        userid = str(userid)

        sql = "INSERT INTO users (userid, username, email, password, phone_number) VALUES (%s, %s, %s, %s, %s)"

        val = (userid, register.username, register.email, register.password, register.phoneNumber)
        cursor.execute(sql, val)

        db.commit()

        return "success"

@app.post("/login")
async def login(login: models.Login):
    cursor = db.cursor()

    sql = "SELECT password FROM users WHERE email = %s"
    val = (login.email,)
    cursor.execute(sql, val)

    result = cursor.fetchall()

    if result:
        # return result
        if result[0][0] == login.password:
            return "success"
        else:
            return "Wrong Email or Password!"
    else:
        return "Wrong Email or Password!"
