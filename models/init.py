from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def init_app(app):
  
  app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', False)
  db.init_app(app)
  print (" ** SQLAlchemy App Initialised")