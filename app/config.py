import os

class Config(object):
   PROJECT = "SampingChuang" 
   
   # Get app root path, also can use flask.root_path.
   PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
   
   SECRET_KEY = 'NeejBmeWu34hyWU2yZeDM2PF2jeWNqNCQjvdf3kp'
