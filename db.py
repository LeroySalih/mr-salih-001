#import pymysql

"""
host = "34.65.137.44"
username = "sleroy"
pwd = "dolphin1234"
dbName = "mrsalih001"

#db = pymysql.connect(host, username, pwd, dbName,  ssl={'ca': './db-scripts/server-ca.pem'})
db = pymysql.connect(host, username, pwd, dbName)

cursor = db.cursor()


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
