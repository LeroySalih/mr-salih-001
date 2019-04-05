from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm 
from flask_debugtoolbar import DebugToolbarExtension

from blueprints.maths import mathsBP
from blueprints.computing import computingBP
from blueprints.users import usersBP



from models.init import init_app

#from db import cursor

import config 
from models import init_db



app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'thisisasecret'
toolbar = DebugToolbarExtension(app)

app.register_blueprint(mathsBP, url_prefix='/maths')
app.register_blueprint(computingBP, url_prefix='/computing')
app.register_blueprint(usersBP, url_prefix='/users')

app.config.from_object(config)
app.config['DEBUG'] = True

init_app(app)

print (' * {dbUri}'.format(dbUri=app.config['SQLALCHEMY_DATABASE_URI']))


@app.route('/') 
def hello():
  return render_template('index.html', results=None)


@app.route('/admin/users')
def admin_users():
  cursor.execute("SELECT * FROM USERS;")
  for x in cursor:
    print(x)
    
  return "Users Admin Page"


if __name__ == '__main__':
  app.run(debug=True)

