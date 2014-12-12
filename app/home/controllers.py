from flask import (Flask, Blueprint, render_template, current_app, request,
                   flash, url_for, redirect, session, abort, jsonify, send_from_directory)


home = Blueprint('home', __name__)

@home.route('/health_check')
def healthy():
   return jsonify(status='good')

@home.route('/')
def index():
   return render_template('index.html')
   