from flask import Flask
from .config import Config
from .home.controllers import home
from .home.tedDemo import tedDemo

# For import *
__all__ = ['create_app']

DEFAULT_BLUEPRINTS = [
   home,
   tedDemo
]

def create_app():
   app = Flask(__name__)
   

   
   #load config
   app.config.from_object(Config)

   configure_blueprints(app, DEFAULT_BLUEPRINTS)
   
   return app

def configure_blueprints(app, blueprints):
   """Configure blueprints in views."""
   
   for blueprint in blueprints:
      app.register_blueprint(blueprint)
