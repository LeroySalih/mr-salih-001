from flask import Blueprint, render_template, abort 

computingBP = Blueprint('computing', __name__, template_folder='templates')

@computingBP.route('/')
def computing():
  return render_template('computing/module-header-computing.html')


@computingBP.route('/databases/<moduleId>')
def computing_databases_intro(moduleId):
  return render_template('computing/databases/{0}.html'.format(moduleId))

@computingBP.route('/p5-intro')
def computing_p5Intro():
  return render_template("computing/p5-intro.html")

@computingBP.route('/models/modelling-with-sketchup')
def computing_sketchUpIntro():
  return render_template("computing/models/modelling-with-sketchup.html")


@computingBP.route('/python-intro')
def computing_python_intro():
  return render_template("computing/python-intro.html")

@computingBP.route('/algorithms')
def computing_algorithms():
  return render_template("computing/algorithms.html")

@computingBP.route('/using-arrays')
def computing_arrays():
  return render_template("computing/using-arrays.html")



@computingBP.route('/web/internet-www')
def computing_internet_www():
  return render_template("computing/web/internet-www.html")

@computingBP.route('/web/intro-html-css-js')
def computing_intro_html():
  return render_template("computing/web/intro-html-css-js.html")

@computingBP.route('/web/web-server')
def computing_web_server():
  return render_template("computing/web/web-server.html")

@computingBP.route('/web/web-design')
def computing_web_design():
  return render_template("computing/web/web-design-with-figma.html")

@computingBP.route('/python/<module>')
def computing_python_challenges(module):
  return render_template("computing/python/{}.html".format(module))

