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

@mathsBP.route('/geometry')
def maths_trig():
  return render_template('maths/geometry/module-header.html')

@mathsBP.route('/geometry/<moduleId>')
def maths_trig_module(moduleId):
  return render_template('maths/geometry/{0}.html'.format(moduleId))

@mathsBP.route('/venn-diagrams')
def maths_venn_diagrams():
  return render_template("venn-diagrams.html")

@mathsBP.route('/functions')
def maths_functions():
  return render_template("maths/functions.html")
  

@mathsBP.route('/mini-projects')
def maths_mini_projects():
  return render_template("maths/mini-projects/module-header.html")

@mathsBP.route('/mini-projects/<moduleId>')
def maths_mini_projects_file(moduleId):
  return render_template("maths/mini-projects/{moduleId}.html".format(moduleId))


@mathsBP.route('/hints')
def maths_hints():
  return render_template("maths/hints/module-header.html")

@mathsBP.route('/hints/<moduleId>')
def maths_hints_file(moduleId):

  return render_template("maths/hints/{moduleId}.html".format(moduleId=moduleId))


