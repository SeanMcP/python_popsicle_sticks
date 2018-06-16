from flask import Flask, jsonify, request
# from utils import shuffle
import json
import uuid

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to the Popsicle Sticks API, powered by Python and Flask!'

# Level routes
@app.route('/levels/student/<student_id>')
def get_levels_by_student(student_id):
    levels = read_file('levels')
    res = list(filter(lambda level: level['student_id'] == student_id, levels))
    return jsonify(res)

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
        with open('./data/sections.json', 'w') as file:
            sections.append(section)
            json.dump(sections, file)
        return 'Success'

@app.route('/section/<id>')
def get_section_by_id(id):
    sections = read_file('sections')
    for section in sections:
        if section['id'] == id:
            return jsonify(section)
        else:
            return 'None found'

# Student routes

@app.route('/students')
def get_list_students():
    res = read_file('students')
    return jsonify(res)

@app.route('/students/name')
def get_list_student_names():
    students = read_file('students')
    res = []
    for student in students:
        res.append(student['name'])
    return jsonify(res)

@app.route('/students/section/<section_id>')
def get_list_students_by_section(section_id):
    students = read_file('students')
    res = []
    for student in students:
        if student['section_id'] == section_id:
            res.append(student)
    return jsonify(res)

@app.route('/student', methods=['POST'])
def post_add_student():
    if request.method == 'POST':
        student_id = gen_id()
        student = {
            'gender': request.form['gender'],
            'id': student_id,
            'name': request.form['name'],
            'section_id': request.form['section_id']
        }
        students = read_file('students')
        with open('./data/students.json', 'w') as file:
            students.append(student)
            json.dump(students, file)

        level = {
            'current_level': request.form['current_level'],
            'section_id': request.form['section_id'],
            'student_id': student_id
        }
        levels = read_file('levels')
        with open('./data/levels.json', 'w') as file:
            levels.append(level)
            json.dump(levels, file)
        return 'Success'

@app.route('/student/<id>')
def get_student_by_id(id):
    students = read_file('students')
    for student in students:
        if student['id'] == id:
            return jsonify(student)
        else:
            return 'None found'

# Utility functions
def read_file(file_name):
    with open(f'./data/{file_name}.json') as raw:
        return json.load(raw)

def gen_id():
    return str(uuid.uuid4())