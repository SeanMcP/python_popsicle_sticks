from flask import Flask
app = Flask(__name__)

students = [ 'Sean' ]

@app.route('/')
def hello_world():
    return 'Hello, World!'