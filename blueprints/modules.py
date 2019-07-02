from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

from models.lo_models import Module

from DAO.module_db import ModuleDB, moduleDB
from DAO.lo_db import LoDB, loDB

modulesBP = Blueprint('modules', __name__, template_folder='templates')

@modulesBP.route('/')
def show_modules():
  try:
    modules = moduleDB.modules.values()
    return render_template('modules/module-header.html', modules=modules)
  except TemplateNotFound:
    print ('Template Not Found error', 'modules/module-header.html' )
    abort(404)
    
@modulesBP.route('/<moduleId>')
def modules_general(moduleId):
  try:
    #get module
    module = moduleDB.findByUrl(moduleId)
    
    if module is None:
      return "No module found"

    moduleDB.populateLessons(module)

    loIds = moduleDB.getAllLOIds(module.id)
    print (f"found loIds {loIds}")
    los = loDB.findByIds(*loIds)
    print (f"found los {los}")
    loGroups = loDB.groupByType(los)


    return render_template(f'modules/module.html', module=module, loGroups=loGroups)
  except TemplateNotFound:
    print ('Template Not Found error', f'modules/module.html' )
    abort(404)

