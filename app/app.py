#!/usr/bin/env python3

from flask import Flask
import ipdb

app = Flask(__name__)

if __name__ == '__main__':
    app.run()

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return param

@app.route('/count/<int:num>')
def count(num):
    nums = range(num)
    string = ''
    for n in nums:
        string += f'{n}\n'
    return string

@app.route('/math/<int:num1><string:operation><int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == "div":
        return str(num1 / num2)
    elif operation == "*":
        return str(num1 * num2)
    else:
        return str(num1 % num2)
