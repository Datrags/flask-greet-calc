# Put your app in here.
from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route('/')
def index():
    return f"""
        <h1>Calculator</h1>
        
        <form action="/math" method="POST">
            <input type="number" name="a" placeholder="a"/>
            <input type="number" name="b" placeholder="b"/>

            <input type="radio" id="add" name='op' value="add"/>
            <label for="add">Add</label>
            <input type="radio" id="sub" name='op' value="sub"/>
            <label for="sub">Subtract</label>
            <input type="radio" id="mult" name='op' value="mult"/>
            <label for="mult">Multiply</label>
            <input type="radio" id="div" name='op' value="div"/>
            <label for="div">Divide</label>
            <button>submit</button>
        </form>

    """

@app.route('/math/', methods=['POST'])
def math_page():
    op = request.form['op']
    
    a = int(request.form['a'])
    b = int(request.form['b'])
    if op == "add":
        return f" {a} + {b} = {add(a,b)}"
    elif op == "sub":
        return f" {a} - {b} = {sub(a,b)}"
    elif op == "mult":
        return f" {a} * {b} = {mult(a,b)}"
    elif op == "div":
        return f" {a} / {b} = {div(a,b)}"