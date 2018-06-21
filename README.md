# Python Popsicle Sticks

This is a Python/Flask API for the [Popsicle Sticks app](https://github.com/SeanMcP/popsicle-sticks).

[Project Board](https://github.com/SeanMcP/python_popsicle_sticks/projects/1)

## Documentation
### Endpoints
#### Levels
- `GET /levels/student/<student_id>` - Returns an array of levels for a given student
#### Section
- `GET /sections` - Returns an array of all sections
- `POST /section` - Adds a new section. Required fields: `stage`, `title`
- `GET /section/<id>` - Returns a section by id
- `POST /section/<id>` - Updates existing section. Optional fields: `stage`, `title`
- `GET /section/remove/<id>` - Removes section from sections, students, and levels
#### Student
- `GET /students` - Returns an array of all students
- `GET /students/name` - Returns an array of student name strings
- `GET /students/section/<section_id>` - Returns an array of students for a given section
- `GET /students/section/none` - Returns an array of students without a section
- `POST /student` - Adds a new student. Required fields: `current_level`, `gender`, `name`, `section_id`
- `GET /student/<id>` - Returns a student by id
- `POST /student/<id>` - Updates existing student. Optional fields: `gender`, `name`
- `GET /student/<student_id>/section/<section_id>` - Adds student to existing section
- `GET /student/<student_id>/remove/section/<section_id>` - Removes student from section
- `GET /student/remove/<id>` - Removes student from students and levels


This project takes some inspiration from [Auth0's](https://auth0.com) ["Developing RESTful APIs with Python and Flask"](https://auth0.com/blog/developing-restful-apis-with-python-and-flask/) tutorial.