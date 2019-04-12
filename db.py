import pymysql
import warnings 
from sql.db import db 
from sql.users import sqlDROP_USER_TABLE, sqlCREATE_USER_TABLE, sqlADD_USERS, sqlREAD_USERS 

from do.users_do import read_all

def show_version(cursor):
  cursor.execute("SELECT VERSION()")
  data = cursor.fetchone()
  print ("Database version: %s " % data)

def initDb(cursor):
  with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    print("Dropping Tables")
    cursor.execute(sqlDROP_USER_TABLE)
    print("Done")

    print ("Creating Tables")
    cursor.execute(sqlCREATE_USER_TABLE)
    print("Done")

    print ("Adding Admin user")
    cursor.execute(sqlADD_USERS)
    print("done")


def listUsers(cursor):
  users = read_all()
  print (users)

    


if (__name__ == "__main__"):

  cursor = db.cursor()
  show_version(cursor)
  #initDb(cursor)
  listUsers(cursor)
  db.close()

