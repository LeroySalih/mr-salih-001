from flask import Blueprint, render_template, abort, current_app as app
from models.init import db
from models.user import User, list_users
from wtforms.validators import InputRequired 
from flask_login import UserMixin, LoginManager, current_user , login_user, current_user, logout_user

#from flask_bcrypt import Bcrypt
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField 

usersBP = Blueprint('users', __name__, template_folder='templates')

#login_manager = LoginManager()
#login_manager.init_app(app)


@usersBP.route('/')
def show_users():
  # app = current_app()
  result = list_users(app)
  print (result)
  
  print ('found', result)
  return render_template('users/index.html', rowCount=len(result), rows=result)

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
  """
  form = LoginForm()
  if form.validate_on_submit():
    return '<H1>The username is {}.  The password is {}.'.format(form.username.data, form.password.data)
  return render_template('users/login.html', form=form)
  """
  u = User.query.filter_by(first_name='admin').first()
  login_user(u)
  return "User Logged In"

@usersBP.route('/logout', methods=['GET', 'POST'])
def show_logout():
  """
  form = LoginForm()
  if form.validate_on_submit():
    return '<H1>The username is {}.  The password is {}.'.format(form.username.data, form.password.data)
  return render_template('users/login.html', form=form)
  """
  #u = current_user # User.query.filter_by(first_name='admin').first()
  logout_user()
  return "User Logged Out"



def register_user(form):
  user = User(first_name = form.first_name.data)

@usersBP.route('/register', methods=['GET', 'POST'])
def show_register():
  form = RegisterForm()

  if form.validate_on_submit():
    register_user(form)
    return render_template('users/register_success.html', form=form)
  
  return render_template('users/register.html', form=form)


@usersBP.route('/check')
def show_check():
  cu = current_user
  print(cu)
  return render_template('users/check.html', cu=cu)




