from flask import Flask, current_app
from flask_login import UserMixin


#[START model]
class User(UserMixin):
  
  id = 0
  first_name = ""

  def __init__(self, dict):
    #Constructor
    for key in dict:
      setattr(self, key, dict[key])

  def __repr__(self):
    return "<User(id={}, first_name='{}')>".format(self.id, self.first_name)
#[END model]




  

  



  #


