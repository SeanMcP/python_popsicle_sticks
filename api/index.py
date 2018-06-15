from flask import Flask, jsonify
# from utils import shuffle
import json

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to the Popsicle Sticks API, powered by Python!'

@app.route('/sections')
def get_sections():
    res = get_data('sections')
    return jsonify(res)

@app.route('/students')
def get_students():
    res = get_data('students')
    return jsonify(res)

# Utility functions
def read_json():
    with open('./api/data.json') as raw:
        return json.load(raw)

def get_data(key):
    return read_json()[key]