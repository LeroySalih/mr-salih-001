from models.user import User
from sql.db import cursor
from sql.users import sqlREAD_USERS

def read_all():
  users = []

  cursor.execute(sqlREAD_USERS)

  results = cursor.fetchall()

  for record in results:
    users.append(User(record))

  return users

def read():
  pass

def create():
  pass

def update():
  pass
