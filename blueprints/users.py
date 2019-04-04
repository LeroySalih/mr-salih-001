from flask import Blueprint, render_template, abort, current_app as app
from models.init import db
from models.user import _create_user
from wtforms.validators import InputRequired 

import models.user  
#from flask_bcrypt import Bcrypt
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField 

usersBP = Blueprint('users', __name__, template_folder='templates')




@usersBP.route('/')
def show_users():
  # app = current_app()
  result = models.user.list_users(app)
  rows=result[0]
  print ('found', result)
  return render_template('users/index.html', rowCount=len(rows), rows=rows)

class LoginForm(FlaskForm):
  username = StringField('username', validators=[InputRequired('A username is required')])
  password = PasswordField('password', validators=[InputRequired('A password is required')])

class RegisterForm(FlaskForm):
  username = StringField('Username', validators=[InputRequired('A username is required')])
  first_name = StringField('First Name', validators=[InputRequired('A First Name is required')])
  family_name = StringField('Family Name', validators=[InputRequired('A Family Name is required')])
  current_form = StringField('Current Form', validators=[InputRequired('A Current Form is required')])
  password = PasswordField('Password', validators=[InputRequired('A password is required')])



@usersBP.route('/login', methods=['GET', 'POST'])
def show_login():
  form = LoginForm()
  if form.validate_on_submit():
    return '<H1>The username is {}.  The password is {}.'.format(form.username.data, form.password.data)
  return render_template('users/login.html', form=form)
  
def register_user(form):
  user = User(first_name = form.first_name.data)

@usersBP.route('/register', methods=['GET', 'POST'])
def show_register():
  form = RegisterForm()

  if form.validate_on_submit():
    register_user(form)
    return render_template('users/register_success.html', form=form)
  
  return render_template('users/register.html', form=form)