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

@app.route('/computing/p5-intro')
def computing_p5Intro():
  return render_template("computing/p5-intro.html")

@app.route('/computing/sketchup-intro')
def computing_sketchUpIntro():
  return render_template("computing/sketchup-intro.html")


@app.route('/computing/web-design')
def computing_web_design():
  return render_template("computing/web-design.html")

@app.route('/computing/python-intro')
def computing_python_intro():
  return render_template("computing/python-intro.html")

@app.route('/computing/algorithms')
def computing_algorithms():
  return render_template("computing/algorithms.html")


@app.route('/computing/web-server')
def computing_web_server():
  return render_template("computing/web-server.html")

@app.route('/maths/venn-diagrams')
def maths_venn_diagrams():
  return render_template("venn-diagrams.html")

if __name__ == '__main__':
  app.run(debug=True)

