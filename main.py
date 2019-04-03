from flask import Flask, render_template, url_for

from blueprints.maths import mathsBP
from blueprints.computing import computingBP

#from db import cursor

import config 

app = Flask(__name__)
app.register_blueprint(mathsBP, url_prefix='/maths')
app.register_blueprint(computingBP, url_prefix='/computing')

app.config.from_object(config)
app.config['DEBUG'] = True

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




@app.route('/maths/venn-diagrams')
def maths_venn_diagrams():
  return render_template("venn-diagrams.html")

@app.route('/maths/functions')
def maths_functions():
  return render_template("maths/functions.html")

@app.route('/maths/past-papers')
def maths_past_papers():
  return render_template("maths/past-papers.html")


@app.route('/db-test')
def db_test():
  
  sql = "SELECT * FROM EMPLOYEE"
  cursor.execute(sql)
  results = cursor.fetchall()
  rows = len(results)
  return render_template('db-test.html', results=rows)

@app.route('/bid/<pid>/<name>/<bid>')
def placeBid(pid, name, bid):
  return render_template('place_bid.html', pid=pid, name=name, bid=bid)

if __name__ == '__main__':
  app.run(debug=True)

