from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index ():
    return render_template ("home.html.jinja")
    user_name = "Nakuzi"

@app.route('/hello/<name>')
def hello(name):
    return f"hello {name}"


@app.route('/ping')

def page2 ():
    return "<p>pong</p>" 
