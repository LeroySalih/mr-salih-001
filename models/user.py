from flask import Flask

from flask_sqlalchemy import SQLAlchemy

import sys
sys.path.append('.')

import config

db=SQLAlchemy()


def from_sql(row):
  data = row.__dict__.copy()
  data['id'] = row.id
  data.pop('_sa_instance_state')
  return data 

#[START model]
class User(db.Model):
  __tablename__ = 'USERS'
  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(255))

  def __repr__(self):
    return "<User(id='{id}', firstName={first_name})>".format(id=id, first_name=first_name)
#[END model]

def list_users(limit=10, cursor=None):
  cursor = int(cursor) if cursor else 0
  query = (User.query
              .order_by(User.first_name)
              .offset(cursor)
              )
  users = list (map(from_sql, query.all()))
  next_page = cursor + limit if len(users) == limit else None
  return (users, next_page)

#[START read]
def read_user(id):
  result = User.query.get(id)
  if not result:
    return None
  return from_sql(result)
#[END read]

#[START user]
def create_user(data):
  user = User(**data)
  db.session.add(user)
  db.session.commit()
  return from_sql(user)
#[END user]

#[START update]
def update_user(data, id):
  user = User.query.get(id)
  for k, v in data.items():
    setattr(user, k, v)
  db.session.commit()
  return from_sql(user)
#[END update]

#[START delete]
def delete_user(id):
  User.query.filter_by(id=id).delete()
  db.session.commit()
#[END delete]





#[START _add_users]
def _list_users(app):
  with app.app_context():
    result = list_users()
    for u in result[0]:
      print (u)
#[END _add_users]

  



  #


