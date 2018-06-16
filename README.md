# Python Popsicle Sticks

This is a Python/Flask API for the [Popsicle Sticks app](https://github.com/SeanMcP/popsicle-sticks).

[Project Board](https://github.com/SeanMcP/python_popsicle_sticks/projects/1)

## Documentation
### Endpoints
#### Levels
- `GET /levels/student/<student_id>` - Returns an array of levels for a given student
#### Section
- `GET /sections` - Returns an array of all sections
- `POST /section` - Adds a new section. Required fields: `title`, `level`
#### Student
- `GET /students` - Returns an array of all students
- `GET /students/name` - Returns an array of student names
- `GET /students/section/<section_id>` - Returns an array of students for a given section
- `GET /student/<id>` - Returns a student by id
- `POST /student` - Adds a new student. Required fields: `current_level`, `gender`, `name`, `section_id`


This project takes some inspiration from [Auth0's](https://auth0.com) ["Developing RESTful APIs with Python and Flask"](https://auth0.com/blog/developing-restful-apis-with-python-and-flask/) tutorial.