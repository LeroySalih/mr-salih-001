from flask import Blueprint, render_template, abort 


usersBP = Blueprint('users', __name__, template_folder='templates')

@usersBP.route('/')
def show_users():
  return render_template('users/index.html')


