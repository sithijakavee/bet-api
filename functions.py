from database import db

def getUserById(id):
    cursor = db.cursor()

    sql = "SELECT * FROM users WHERE email = %s"
    val = (id,)
    cursor.execute(sql, val)

    result = cursor.fetchall()

    for x in result:
        return(x)
