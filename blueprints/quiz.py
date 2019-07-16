from flask import Blueprint, render_template, abort, request, current_app as app
from jinja2 import TemplateNotFound

from DAO.class_db import classDB
from DAO.module_db import ModuleDB, moduleDB
from DAO.quiz_db import quizDB 

from flask_login import current_user

import json 


quizBP = Blueprint('quiz', __name__, template_folder='templates')

@quizBP.route('/')
def show_quiz_viewer():
  try:
    classes = classDB.classes
    return render_template('quiz/quiz-view.html', classes=classes)
    
  except TemplateNotFound:
    abort(404)
    
@quizBP.route('/<quizId>')
def modules_general(quizId):
  try:
    return render_template(f'quiz/quiz.html')
    
  except TemplateNotFound:
    app.logger.error('Template Not Found')
    abort(404)


@quizBP.route('/check/<moduleId>/<lessonId>/<activityId>', methods = ['POST'])
def modules_check_quiz_answers(moduleId, lessonId, activityId):
    """
    modules_check_quiz_answers:
    Checks the values passed from the client against the correct values in the quiz.
    """

    #Get the form data
    d = request.form['data']
    
    #parse the  text data into an object
    answers = json.loads(d)
    
    #get the correct answers from the appropriate quiz (remember a lesson may have more than 1 quiz.) 
    lesson = moduleDB.findLessonByIds(moduleId, lessonId)
    activity = lesson.activities[int(activityId)]
    quiz = activity.quiz 

    #Calculate correct percentage. 
    score = quiz.check_answers(answers) / len(list(quiz.questions.keys()))
    
    if current_user != None:
      app.logger.info(f'Saving attempt for user id: {current_user.id}.')
      quizDB.save_attempt(current_user.id, moduleId, lessonId, activityId, score, answers)

    #Return the correct score.
    return f'{{"result":{score} }}'
 


