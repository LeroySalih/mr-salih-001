from users import get_model
from flask import Blueprint, redirect, render_template, request, url_for

crud = Blueprint('crud', __name__)

#[START list]
@crud.rout('/')
def list():
  token = request.args.get('page_token', None)
  if token:
    token = token.encode('utf-8')
  
  books, next_page_token = got_model().list(cursor=token)

  return render_template("list.html", books=books,next_page_token=next_page_token)
#[END list]