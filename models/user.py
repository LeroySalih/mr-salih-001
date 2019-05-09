from flask import Flask, current_app
from flask_login import UserMixin

from werkzeug.security import generate_password_hash, check_password_hash

from sql.db import get_db
from sql.users import sqlREAD_USERS, sqlREAD_USER, sqlREAD_USER_BY_FIRST_NAME, sqlREAD_USER_BY_USERNAME, sqlDROP_USER_TABLE, sqlCREATE_USER_TABLE, sqlADD_USERS


class UserException (Exception):

  def __init__(self, expression, message):
        self.expression = expression
        self.message = message


#[START model]
class User(UserMixin):
  
  id = 0
  first_name = ""
  __username = "not set"
  __password = "not set"

  def __init__(self, dict):

    if (dict == None):
      raise UserException(dict, "Dictionary is None.  This is not allowed when creating a User object.")

    #Constructor
    for key in dict:
      setattr(self, key, dict[key])

  def __repr__(self):
    return "<User(id={}, first_name='{}', username='{}', password='{}')>".format(self.id, self.first_name, self.username, self.password)


  def to_dict(self):
    return {'id': self.id, 'first_name': self.first_name, 'username': self.__username, 'password': self.password}
  

  def set_pw(self, pw):
    self.__password = generate_password_hash(pw)
   
  
  def check_pw(self, val):
    return check_password_hash(self.__password, val)

  @property
  def username(self):
    return self.__username
  
  @username.setter
  def username(self, val):
    self.__username = val

  @property
  def password(self):
    return self.__password

  @password.setter
  def password(self, val):
    self.__password = val
  

  @staticmethod
  def get_all():
    users = []

    db = get_db()
    cursor = db.cursor()
    cursor.execute(sqlREAD_USERS)

    results = cursor.fetchall()

    for record in results:
      users.append(User(record))

    db.close()
    return users

  @staticmethod
  def get_by_id(id): 
    db = get_db()
    cursor = db.cursor()
    cursor.execute(sqlREAD_USER.format(id))
    result = cursor.fetchone()
    db.close()
    if result == None: 
      return None
    return User(result) 

  @staticmethod 
  def get_by_first_name(first_name):
    users = []
    db = get_db()
    cursor = db.cursor()
    cursor.execute(sqlREAD_USER_BY_FIRST_NAME.format(first_name))
    for record in cursor.fetchall():
      users.append(User(record))
    db.close()
    return users

  @staticmethod
  def get_by_username(username):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(sqlREAD_USER_BY_USERNAME.format(username))
    user = cursor.fetchone()
    db.close()
    if user == None:
      return None 
    else: 
      return User(user)


  @staticmethod
  def add_user(u):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(sqlADD_USERS.format(first_name=u.first_name, username=u.username, password=u.password))
    #reload user with ID
    u = User.get_by_username(u.username)
    db.close()
    return u
    
  
  @staticmethod
  def create_tables():
    db = get_db()
    cursor = db.cursor()
    cursor.execute(sqlDROP_USER_TABLE)
    cursor.execute(sqlCREATE_USER_TABLE)
    db.close()
    


  @staticmethod
  def from_form(form):
    userDict = { 'first_name': form.first_name.data, 'username': form.username.data }
    u = User(userDict)
    if len(form.password.data):
      u.set_pw(form.password.data)
    return u
    


#[END model]




  

  



  #


