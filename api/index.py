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
    levels_by_student = list(filter(lambda level: level['student_id'] == student_id, levels))
    sections = read_file('sections');
    for level in levels_by_student:
        for section in sections:
            if section['id'] == level['section_id']:
                level['section_title'] = section['title']
    
    return jsonify(levels_by_student)

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
        sections.append(section)
        write_data_to_file(sections, 'sections')
    
        return RESPONSE.SUCCESS

@app.route('/section/<id>')
def get_section_by_id(id):
    sections = read_file('sections')
    for section in sections:
        if section['id'] == id:
            return jsonify(section)
    
    return RESPONSE.NONE

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
        if section_id in student['section_id']:
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
            'section_id': list(request.form['section_id'])
        }
        students = read_file('students')
        students.append(student)
        write_data_to_file(students, 'students')

        level = {
            'current_level': request.form['current_level'],
            'section_id': request.form['section_id'],
            'student_id': student_id
        }
        levels = read_file('levels')
        levels.append(level)
        write_data_to_file(levels, 'levels')
        
        return RESPONSE.SUCCESS

@app.route('/student/<id>', methods=['GET', 'POST'])
def get_student_by_id(id):
    students = read_file('students')
    if request.method == 'GET':
        for student in students:
            if student['id'] == id:
                return jsonify(student)
        
        return RESPONSE.NONE

    elif request.method == 'POST':
        i = find_index_by_key_value(students, 'id', id)
        student = students[i]
        del students[i]
        for key in request.form:
            student[key] = request.form[key]
        students.append(student)
        write_data_to_file(students, 'students')

        return RESPONSE.SUCCESS

@app.route('/student/<student_id>/section/<section_id>', methods=['POST'])
def add_student_to_section(student_id, section_id):
    if request.method == 'POST':
        students = read_file('students')
        for student in students:
            if student['id'] == student_id:
                student['section_id'].append(section_id)
                write_data_to_file(students, 'students')
                return RESPONSE.SUCCESS
            else:
                return RESPONSE.NONE

# Utilities
def find_index_by_key_value(list, key, value):
    for i, item in enumerate(list):
        if item[key] == value:
            return i
    return None

def gen_id():
    return str(uuid.uuid4())

def read_file(file_name):
    with open(f'./data/{file_name}.json') as raw:
        return json.load(raw)

def write_data_to_file(data, file_name):
    with open(f'./data/{file_name}.json', 'w') as file:
        json.dump(data, file)

RESPONSE = {
    'FAIL': 'Failed to execute',
    'NONE': 'None found',
    'SUCCESS': 'Success'
}