from flask import Blueprint, render_template, abort 

indexBP = Blueprint('indexBP', __name__, template_folder='templates')

@indexBP.route('/')
def index():
  return render_template('index.html', results=None)