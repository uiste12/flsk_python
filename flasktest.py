#!/bin/python3

from flask import Flask

app = Flask(__name__)#flask init

@app.route("/")#decorator
def index():
    return "Hello world from the server !!"

app.run(host="0.0.0.0" , port=80)#flask run  
