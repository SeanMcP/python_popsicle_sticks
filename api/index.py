from flask import Flask
# from utils import shuffle
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/students')
def get_students():
    return 'Students'

# Utility functions
def read_json():
    with open('./api/data.json') as raw:
        data = json.load(raw)
    return data 

def get_data(key):
    return read_json()[key]