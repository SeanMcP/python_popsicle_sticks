from flask import Flask
from utils import shuffle

app = Flask(__name__)

students = [ 'Sean' ]

@app.route('/')
def hello_world():
    return 'Hello, World!'