import mysql.connector

db = mysql.connector.connect(
  host="banana.cnrmem3900ov.ap-south-1.rds.amazonaws.com",
  user="admin",
  password="20030609s",
  database="bet_db"
)

# db = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="bet_db"
# )
