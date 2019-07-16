from flask import Blueprint, render_template, abort, request
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
    
    los = loDB.findByIds(*loIds)
    
    loGroups = loDB.groupByType(los)


    return render_template(f'modules/module.html', module=module, loGroups=loGroups)
  except TemplateNotFound:
    print ('Template Not Found error', f'modules/module.html' )
    abort(404)



@modulesBP.route('/<moduleId>/<lessonId>')
def modules_lesson(moduleId, lessonId):

  try:
    module = moduleDB.findById(moduleId)
    lesson = module.lessons.get(lessonId)
    loIds = lesson.los 
    los = loDB.findByIds(*loIds)
    loGroups = loDB.groupByType(los)

    return render_template(f'modules/lesson.html', module=module, lesson=lesson, loGroups=loGroups)
 
  except TemplateNotFound:
    print ('Template Not Found error', f'modules/lesson.html' )
    abort(404)



@modulesBP.route('/<moduleId>/<lessonId>/activity')
def modules_lesson_activity (moduleId, lessonId):
  index = int(request.args.get('index', 0))
  module = moduleDB.findById(moduleId)
  lesson = moduleDB.findLessonByIds(moduleId, lessonId)
  # findPastAnswers = quizDB.findPastAnswers('userId', moduleId, lessonId)
  pastAnswers = {1:                                             #Activity Index
                          {0:[False, False, True, False]}       #Question Checkboxes
                    }
  
  return render_template('modules/activities.html', module=module, lesson=lesson, index=index, pastAnswers=pastAnswers)