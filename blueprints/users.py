from flask import Blueprint, render_template, abort, current_app as app


import models.user  

usersBP = Blueprint('users', __name__, template_folder='templates')

@usersBP.route('/')
def show_users():
  # app = current_app()
  result = models.user.list_users(app)
  rows=result[0]
  print ('found', result)
  return render_template('users/index.html', rowCount=len(rows), rows=rows)


