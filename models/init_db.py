from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from init import db, init_app 
from user import  User, list_users 

import config
import models
# db=SQLAlchemy()


#[START createDB]
def create_database(app):
  with app.app_context():
    db.reflect()
    db.drop_all()
    db.create_all()
    print ('All tables created')
#[END createDB]


#[START _add_users]
def add_test_users(app):

  with app.app_context():
    user1 = User(first_name='person1')
    db.session.add(user1)
    admin = User(first_name='admin')
    db.session.add(admin)
    db.session.commit()
    print ('Users Added')
#[END _add_users]


#execute this script by python models/init_db.py
#this script will initialise the database

# To start the proxy server:
# /Users/leroy/cloud_sql_proxy -instances="flask003:europe-west6:mrsalih-com"=tcp:3306


if __name__ == '__main__':
  app = Flask(__name__)
  app.config.from_object(config)
  init_app(app)
  create_database(app)
  add_test_users(app)
  list_users (app)