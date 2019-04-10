from flask import Blueprint, render_template, abort, current_app as app
from flask_login import LoginManager, login_user, login_required
from models.init import db
from models.user import User, _create_user, _list_users, login_manager
from wtforms.validators import InputRequired 

import models.user  
#from flask_bcrypt import Bcrypt
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField 

loginBP = Blueprint('login', __name__, template_folder='templates')

#FlaskLogin Initialisation
#login_manager = LoginManager()
#login_manager.init_app(app)



@loginBP.route('/')
def show_login():
  with app.app_context():
   u = User.query.filter_by(first_name='admin').first()
   login_user(u)
  return "Login - BI {}".format(u.first_name)

@loginBP.route('/logout')
def show_logout():
  return "Logout - TBI"


@loginBP.route('/private')
@login_required
def show_private():
  return "Looking at private data."

@loginBP.route('/init')
def show_init():

  with app.app_context():
    db.create_all()
    #db.metadata.reflect(bind=db.engine)
    u = User(first_name="admin")
    db.session.add(u)
    db.session.commit()

    return "DB Created"

@loginBP.route('/check')
def check():

  return "Check - TBI"



