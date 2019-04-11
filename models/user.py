from flask import Flask, current_app
from flask_login import UserMixin

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

import sys
sys.path.append('.')

from models.init import db 
import config

# db=SQLAlchemy()
#login_manager = LoginManager()
#bcrypt = Bcrypt(current_app

def check_password (hash, pwd):
  return bcrypt.check_password_hash(pwd, password)

def hash_password (pwd):
  return bcrypt.generate_password_hash(pwd) 


def from_sql(row):
  data = row.__dict__.copy()
  data['id'] = row.id
  data.pop('_sa_instance_state')
  u = User()
  u.id = data['id']
  u.first_name = data['first_name']
  print ('*** fromSql:', u)
  return u 

#[START model]
class User(db.Model, UserMixin):
  __tablename__ = 'USERS'
  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(255))

  def __repr__(self):
    return "<User(id='{}', firstName={})>".format(self.id, self.first_name)
#[END model]


#[START Login Manager Scripts]
"""
@login_manager.user_loader
def load_user(user_id):
  user = User.query.filter_by(id=user_id).first()

  if user:
    return user 
  else: 
    return None
"""
#[END Login_manager_scripts]


def _list(limit=10, cursor=None):
  cursor = int(cursor) if cursor else 0
  query = (User.query
              .order_by(User.first_name)
              .offset(cursor)
              )
  users = list (map(from_sql, query.all()))
  next_page = cursor + limit if len(users) == limit else None
  return (users, next_page)

#[START read]
def _read(id):
  print ('*** read called')
  result = User.query.get(id)
  if not result:
    print('result was none')
    return None
  return from_sql(result)
#[END read]

#[START user]
def _create(data):
  user = User(**data)
  db.session.add(user)
  db.session.commit()
  return from_sql(user)
#[END user]

#[START update]
def _update(data, id):
  user = User.query.get(id)
  for k, v in data.items():
    setattr(user, k, v)
  db.session.commit()
  return from_sql(user)
#[END update]

#[START delete]
def _delete(id):
  User.query.filter_by(id=id).delete()
  db.session.commit()
#[END delete]





#[START list_users]
def list_users(app):
  with app.app_context():
    result = _list()
    print ("Found {} rows".format(len(result[0])))
    for u in result[0]:
      print (u)
    return result[0]
#[END list_users]

#[START create_user]
def create_user(app, user):
  with app.app_context():
    return _create(user)
#END create_user]

  

  



  #


