# app/app.py
from flask import Flask # type: ignore
import mysql.connector
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello"

@app.route('/data')
def get_data():
    return "data"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
