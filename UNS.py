from flask import Flask, render_template, url_for
import requests
import json

app = Flask(__name__)

r = requests.get('https://unstats.un.org/SDGAPI/v1/sdg/Goal/List?includechildren=true')
dataGoals = json.loads(r.text)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/goals')
def goals():
    return render_template('goals.html', goalList=dataGoals)

@app.route('/documents')
def documents():
    return render_template('documents.html')

@app.route('/milestones')
def milestones():
    return render_template('milestones.html')

@app.route('/statements')
def statements():
    return render_template('statements.html')

@app.route('/progress')
def progress():
    return render_template('progress.html')

@app.route('/more-info')
def moreInfo():
    return render_template('more-info.html')