from flask import Flask, render_template, url_for
import pymysql

#db = pymysql.connect("127.0.0.1", "root", "cardiff1", "lessons")


app = Flask(__name__)
# api = Api(app)




app.config['DEBUG'] = True


@app.route('/')
def hello():
  #cursor = db.cursor()
  #sql = "SELECT * FROM tasks"
  #cursor.execute(sql)
  #results = cursor.fetchall()
  return render_template('index.html', results=None)

@app.route('/p5-intro')
def p5Intro():
  return render_template("p5-intro.html")

@app.route('/sketchup-intro')
def sketchUpIntro():
  return render_template("sketchup-intro.html")

@app.route('/html-basics')
def htmlBasics():
  return render_template("html-basics.html")

if __name__ == '__main__':
  app.run(debug=True)

