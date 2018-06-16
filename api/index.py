from flask import Flask, jsonify, request
# from utils import shuffle
import json
import uuid

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to the Popsicle Sticks API, powered by Python!'

# Section routes

@app.route('/sections')
def get_list_sections():
    res = read_file('sections')
    return jsonify(res)

@app.route('/section', methods=['POST'])
def post_add_section():
    if request.method == 'POST':
        section = {
            'id': gen_id(),
            'level': request.form['level'],
            'title': request.form['title']
        }
        sections = read_file('sections')
        with open('./api/sections.json', 'w') as file:
            sections.append(section)
            json.dump(sections, file)
        return 'Success'

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

def read_file(file_name):
    with open(f'./api/{file_name}.json') as raw:
        return json.load(raw)

def gen_id():
    return str(uuid.uuid4())

def get_data(key):
    return read_json()[key]