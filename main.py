
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import db
from functions import getUserById
import models
import uuid

app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://bet-evolution.web.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Bet Api"}


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

    sql = "SELECT userid, password, username, status FROM users WHERE email = %s"
    val = (login.email,)
    cursor.execute(sql, val)
    data = {}
    result = cursor.fetchall()

    if result:
        # return result
        if result[0][1] == login.password:
            data["status"] = "success"
            data["username"] = result[0][2]
            data["userid"] = result[0][0]
            data["user_type"] = result[0][3]
            return data
        else:
            data["status"] = "Wrong Email or Password!"
            return data
    else:
        data["status"] = "Wrong Email or Password!"
        return data

# @app.get("/get_live_events_by_league_id")
# def get_live_events_by_league_id():
#     url = ''

@app.get("/get_users")
async def get_users():
    cursor = db.cursor()

    sql = "SELECT userid, username, email, status FROM users"
    cursor.execute(sql)
    data = []
    result = cursor.fetchall()

    for user in result:
        data.append(
            {
                "userid" : user[0],
                "username" : user[1],
                "email" : user[2],
                "user_type" : user[3] 
            }
        )

    return data


@app.post("/post_bet")
async def post_bet(bet: models.Bet):
    cursor = db.cursor()

    betid = uuid.uuid1()
    betid = str(betid)

    sql = "INSERT INTO bets (userid, username, betid, bet_amount, bet_event, bet_sport, bets) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (bet.userid, bet.username, betid, bet.bet_amount, bet.bet_event, bet.bet_sport, bet.bets)

    cursor.execute(sql, val)

    db.commit()

    return "success"
