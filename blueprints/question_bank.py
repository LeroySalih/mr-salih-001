
from flask import Blueprint, render_template, abort 
from sql.db import db, cursor

question_bank_BP = Blueprint('questions', __name__, template_folder='templates')

@question_bank_BP.route('/')
def show_maths():
  try:
    return render_template('question-bank/index.html')
  except TemplateNotFound:
    abort(404)

@question_bank_BP.route('/quiz/create')
def quiz_create():
  cursor.execute("SELECT * FROM QUIZ_QUESTIONS")
  data = cursor.fetchall()
  
  return "Creating A quiz"


@question_bank_BP.route('/quiz/<quiz_id>')
def quiz_show(quiz_id):
  return "Showing Quiz {}".format(quiz_id)



