from flask import Blueprint, render_template, abort 

mathsBP = Blueprint('maths', __name__, template_folder='templates')

@mathsBP.route('/')
def show_maths():
  try:
    return render_template('maths/module-header-maths.html')
  except TemplateNotFound:
    abort(404)
    
@mathsBP.route('/algebra')
def maths_algebra():
  return render_template('maths/algebra/module-header-algebra.html')

@mathsBP.route('/algebra/<moduleId>')
def maths_algebra_simplifying(moduleId):
  return render_template('maths/algebra/{0}.html'.format(moduleId))

@mathsBP.route('/trig')
def maths_trig():
  return render_template('maths/trig/module-header-trig.html')

@mathsBP.route('/trig/<moduleId>')
def maths_trig_module(moduleId):
  return render_template('maths/trig/{0}.html'.format(moduleId))

@mathsBP.route('/venn-diagrams')
def maths_venn_diagrams():
  return render_template("venn-diagrams.html")

@mathsBP.route('/functions')
def maths_functions():
  return render_template("maths/functions.html")

@mathsBP.route('/past-papers')
def maths_past_papers():
  return render_template("maths/past-papers.html")