import pymysql

db = pymysql.connect("remotemysql.com","Xtt8yYyjlx","nuFUdHOy80","Xtt8yYyjlx" )

cursor = db.cursor()

"""
import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="cardiff1",
  database="lessons"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)

mycursor.execute("SELECT * FROM tasks;")


for x in mycursor:
  print(x)
"""
