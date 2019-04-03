from flask import Flask

from flask_sqlalchemy import SQLAlchemy

import sys
sys.path.append('.')

import config

db=SQLAlchemy()

builtin_list = list 


def init_app(app):
  app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', False)
  db.init_app(app)

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

def list(limit=10, cursor=None):
  cursor = int(cursor) if cursor else 0
  query = (User.query
              .order_by(User.first_name)
              .offset(cursor)
              )
  users = builtin_list (map(from_sql, query.all()))
  next_page = cursor + limit if len(users) == limit else None
  return (users, next_page)

#[START read]
def read(id):
  result = User.query.get(id)
  if not result:
    return None
  return from_sql(result)
#[END read]

#[START user]
def create(data):
  user = User(**data)
  db.session.add(user)
  db.session.commit()
  return from_sql(user)
#[END user]

#[START update]
def update(data, id):
  user = User.query.get(id)
  for k, v in data.items():
    setattr(user, k, v)
  db.session.commit()
  return from_sql(user)
#[END update]

#[START delete]
def delete(id):
  User.query.filter_by(id=id).delete()
  db.session.commit()
#[END delete]

#[START createDB]
def _create_database(app):
  
  with app.app_context():
    db.drop_all()
    db.create_all()
    print ('All tables created')
    
  
#[END createDB]

#[START _add_users]
def _add_users(app):

  with app.app_context():
    user1 = User(first_name='person1')
    db.session.add(user1)
    admin = User(first_name='admin')
    db.session.add(admin)
    db.session.commit()
    print ('Users Added')
#[END _add_users]

#[START _add_users]
def _listUsers(app):
  with app.app_context():
    result = list()
    for u in result[0]:
      print (u)
#[END _add_users]

  


if __name__ == '__main__':
  app = Flask(__name__)
  app.config.from_object(config)
  init_app(app)
  _create_database(app)
  _add_users(app)
  _listUsers (app)
  #


