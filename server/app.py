#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<parameter>')
def print_message(parameter):
    print(parameter)
    return parameter

@app.route('/count/<parameter>')
def count(parameter):
    try:
        number = int(parameter)
        output = '\n'.join(str(i) for i in range(number)) + '\n'
        return output
    except ValueError:
        return "Please provide a valid integer."
    
@app.route('/math/<parameter>')
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def do_math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return "Division by zero is undefined", 400
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Unsupported operation", 400

    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)