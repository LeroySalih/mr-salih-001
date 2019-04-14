from flask import Flask, render_template, url_for, session
from flask_login import LoginManager

from models.user import User

#from flask_wtf import FlaskForm 
#from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
#from flask_debugtoolbar import DebugToolbarExtension



from blueprints.index import indexBP
from blueprints.maths import mathsBP
from blueprints.computing import computingBP
from blueprints.users import usersBP
#from blueprints.login import loginBP





#from db import cursor

import config 


app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisisasecret'
app.config.from_object(config)
app.config['DEBUG'] = True
app.debug = True

#SQLAlchemy Initialisation

login_manager = LoginManager()
login_manager.init_app(app)



@login_manager.user_loader
def load_user(user_id):
  try:

    u = User.get_by_id(user_id)
    if (u == None):
      raise ValueError("A user with id of {user_id} was not found.".format(user_id=user_id))
    return u

  except ValueError as err:
    print (err.args)

  


#toolbar = DebugToolbarExtension(app)
app.register_blueprint(indexBP)
app.register_blueprint(mathsBP, url_prefix='/maths')
app.register_blueprint(computingBP, url_prefix='/computing')
app.register_blueprint(usersBP, url_prefix='/users')
#app.register_blueprint(loginBP, url_prefix='/login')



# print (' * {dbUri}'.format(dbUri=app.config['SQLALCHEMY_DATABASE_URI']))

if __name__ == '__main__':
  app.run(debug=True)

