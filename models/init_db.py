from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models.user import  User, _list_users 

import config

db=SQLAlchemy()



#[START createDB]
def _create_database(app):
  with app.app_context():
    db.reflect()
    db.drop_all()
    db.create_all()
    print ('All tables created')
#[END createDB]


#[START _add_users]
def _add_test_users(app):

  with app.app_context():
    user1 = User(first_name='person1')
    db.session.add(user1)
    admin = User(first_name='admin')
    db.session.add(admin)
    db.session.commit()
    print ('Users Added')
#[END _add_users]

if __name__ == '__main__':
  app = Flask(__name__)
  app.config.from_object(config)
  init_app(app)
  _create_database(app)
  _add_test_users(app)
  _list_users (app)