from flask import Blueprint, session, render_template, abort, current_app as app, redirect 

from models.user import User
from wtforms.validators import InputRequired 
from flask_login import UserMixin, LoginManager, current_user , login_user, current_user, logout_user

#from flask_bcrypt import Bcrypt
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField




usersBP = Blueprint('users', __name__, template_folder='templates')


@usersBP.route('/')
def show_users():
  users = User.get_all()
  return render_template('users/index.html', rowCount=len(users), users=users, )

class LoginForm(FlaskForm):
  username = StringField('Username', validators=[InputRequired('A username is required')])
  password = PasswordField('Password', validators=[InputRequired('A password is required')])
  submit_button = SubmitField('Submit')
  
class RegisterForm(FlaskForm):
  username = StringField('Username', validators=[InputRequired('A username is required')])
  first_name = StringField('First Name', validators=[InputRequired('A First Name is required')])
  password = PasswordField('Password', validators=[InputRequired('A password is required')])
  submit_button = SubmitField('Submit')


def do_login(u):
    login_user(u)
    session['logged_in'] = True
    session['user'] = u.to_dict()


@usersBP.route('/login', methods=['GET', 'POST'])
def show_login():
  
  form = LoginForm()
  if form.validate_on_submit():
    u = User.get_by_username(form.username.data)
    if u != None and u.check_pw(form.password.data):
      do_login(u)
      app.logger.info('%s login OK', u.username)
      return redirect('/')
      
    else:
      app.logger.info('%s login FAILED', u.username)
      return render_template('users/login.html', form=form, message="Invalid Login Details")
      
  else:
    return render_template('users/login.html', form=form, message="")
  
  
@usersBP.route('/logout', methods=['GET', 'POST'])
def show_logout():
  
  logout_user()
  app.logger.info('logout OK')
  if ('logged_in' in session):
    session.pop('logged_in')
  return redirect('/')



def register_user(form):
  user = User(first_name = form.first_name.data)

@usersBP.route('/register', methods=['GET', 'POST'])
def show_register():
  form = RegisterForm()

  if form.validate_on_submit():
    #register_user(form)
    u = User.from_form(form)
    
    u = User.add_user(u)
    do_login(u)
    return render_template('users/register_success.html', user=u)
  
  return render_template('users/register.html', form=form)


@usersBP.route('/check')
def show_check():
  cu = current_user
  return render_template('users/check.html', cu=cu)


@usersBP.route('/create')
def show_create():
  User.create_tables()
  app.logger.info('DB Created OK')
  return "DB Created"




