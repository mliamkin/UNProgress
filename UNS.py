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
