import logging 
from flask import current_app, Flask, redirect, url_for

def create_app(config, debug=False, testing=False, config_overrides=None):
  app = Flask(__name__)
  app.config.from_object(config)
  app.debug = debug
  app.testing = testing 

  if (config_overrides):
    app.config_overrides:
    app.config.update(config_overrides)
  
  with app.app_context():
    model = get_model()
    model.init_app(app)

  from .crud import crud 
  app.register_blueprint(crud, url_prefix='/books')

def get_model():
  model_backend = current_app.config['DATA_BACKEND']
  from . import model_cloudsql 
  model = model_cloudsql
  return model 