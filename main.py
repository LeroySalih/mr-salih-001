from flask import Flask, render_template, url_for


from db import cursor

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/')
def hello():
  return render_template('index.html', results=None)

@app.route('/maths')
def maths():
  return render_template('module-header-maths.html')


@app.route('/computing')
def computing():
  return render_template('module-header-computing.html')

@app.route('/computing/p5-intro')
def computing_p5Intro():
  return render_template("computing/p5-intro.html")

@app.route('/computing/models/modelling-with-sketchup')
def computing_sketchUpIntro():
  return render_template("computing/models/modelling-with-sketchup.html")


@app.route('/computing/python-intro')
def computing_python_intro():
  return render_template("computing/python-intro.html")

@app.route('/computing/algorithms')
def computing_algorithms():
  return render_template("computing/algorithms.html")

@app.route('/computing/using-arrays')
def computing_arrays():
  return render_template("computing/using-arrays.html")



@app.route('/computing/web/internet-www')
def computing_internet_www():
  return render_template("computing/web/internet-www.html")

@app.route('/computing/web/intro-html-css-js')
def computing_intro_html():
  return render_template("computing/web/intro-html-css-js.html")

@app.route('/computing/web/web-server')
def computing_web_server():
  return render_template("computing/web/web-server.html")

@app.route('/computing/web/web-design')
def computing_web_design():
  return render_template("computing/web/web-design-with-figma.html")




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

