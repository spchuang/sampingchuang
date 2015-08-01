from flask import (Flask, Blueprint, render_template, current_app, request,
                   flash, url_for, redirect, session, abort, jsonify, send_from_directory)


home = Blueprint('home', __name__)

@home.route('/health_check')
def healthy():
   return jsonify(status='good')
   
@home.route('/videojs-markers')
def videojs_markers():
   return render_template('videojs-markers.html');

@home.route('/videojs-caption')
def videojs_caption():
   return render_template('videojs-caption.html');

@home.route('/')
def index():
   return ''; render_template('index.html')
   