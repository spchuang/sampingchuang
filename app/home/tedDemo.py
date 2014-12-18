from flask import (Flask, Blueprint, render_template, current_app, request,
                   flash, url_for, redirect, session, abort, jsonify, send_from_directory)
import json
import urllib2

tedDemo = Blueprint('tedDemo', __name__)

LINK = "http://www.ted.com/talks/subtitles/id/1569/lang/%s"

LANGUAGES = [ 'eng', 'zh-tw']

def convertLine(lineData, position, alignment):
   offset = 15000
   return {
      'data': lineData['content'],
      'startTime': lineData['startTime'] + offset ,
      'endTime': lineData['startTime'] + lineData['duration'] + offset,
      'position': position,
      'alignment': alignment
   }


@tedDemo.route('/tedDemo/convertSubtitle')
def convertSubtitle():
   subtitles = []
   
   # download the subtitles
   for lang in LANGUAGES:
      data = urllib2.urlopen(LINK % lang)
      j = json.load(data)
      subtitles.append(j['captions'])
      #k = [i for i, j, k in j[1]]
      #l = json.dumps(k)

   # transform the videojs-caption format
   result = []
   
   i = 0
   length = len(subtitles[0])
   while i < length:
      result.append(convertLine(subtitles[0][i], 'HB', 'CH'))
      result.append(convertLine(subtitles[1][i], 'HT', 'CH'))
      i+=1

   return jsonify(data=result, status='good')