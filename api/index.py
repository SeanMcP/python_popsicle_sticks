from flask import Flask, jsonify
# from utils import shuffle
import json

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to the Popsicle Sticks API, powered by Python!'

# Section routes

@app.route('/sections')
def get_list_sections():
    res = get_data('sections')
    return jsonify(res)

# Student routes

@app.route('/students')
def get_list_students():
    res = get_data('students')
    return jsonify(res)

@app.route('/students/name')
def get_list_student_names():
    students = get_data('students')
    res = []
    for student in students:
        res.append(student['name'])
    return jsonify(res)

@app.route('/student/<id>')
def get_student_by_id(id):
    students = get_data('students')
    for student in students:
        if student['id'] == id:
            return jsonify(student)
        else:
            return 'None found'

# Utility functions
def read_json():
    with open('./api/data.json') as raw:
        return json.load(raw)

def get_data(key):
    return read_json()[key]