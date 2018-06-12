from flask import Flask
# from utils import shuffle
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/students')
def get_students():
    with open('data.json') as data:
        print(json.load(data))
    return 'Students'