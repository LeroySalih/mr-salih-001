from flask import Flask, current_app
from flask_login import UserMixin


from sql.db import cursor
from sql.users import sqlREAD_USERS, sqlREAD_USER, sqlREAD_USER_BY_FIRST_NAME, sqlREAD_USER_BY_USERNAME_PWD, sqlDROP_USER_TABLE, sqlCREATE_USER_TABLE, sqlADD_USERS

#[START model]
class User(UserMixin):
  
  id = 0
  first_name = ""

  def __init__(self, dict):
    #Constructor
    for key in dict:
      setattr(self, key, dict[key])

  def __repr__(self):
    return "<User(id={}, first_name='{}')>".format(self.id, self.first_name)


  def to_dict(self):
    return {'id': self.id, 'first_name': self.first_name}
  """
  def __str__(self):
    return "{'id':{id}, 'first_name':{first_name}}".format(id=self.id, first_name=self.first_name)
  """

  @staticmethod
  def get_all():
    users = []

    cursor.execute(sqlREAD_USERS)

    results = cursor.fetchall()

    for record in results:
      users.append(User(record))

    return users

  @staticmethod
  def get_by_id(id): 
    cursor.execute(sqlREAD_USER.format(id))
    result = cursor.fetchone()
    return User(result) 

  @staticmethod 
  def get_by_first_name(first_name):
    users = []
    cursor.execute(sqlREAD_USER_BY_FIRST_NAME.format(first_name))
    for record in cursor.fetchall():
      users.append(User(record))
    
    return users

  @staticmethod
  def get_by_uname_pwd(username, pwd):
    cursor.execute(sqlREAD_USER_BY_USERNAME_PWD.format(username, pwd))
    user = cursor.fetchone()
    if user == None:
      return None 
    else: 
      return User(user)
  
  @staticmethod
  def create_tables():
    cursor.execute(sqlDROP_USER_TABLE)
    cursor.execute(sqlCREATE_USER_TABLE)
    cursor.execute(sqlADD_USERS.format('admin', 'admin', 'password'))
    


#[END model]




  

  



  #


