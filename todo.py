from flask import Flask, render_template, request

app = Flask(__name__)

todos = ["Hang out with friend", "Play on my computer"]

@app.route('/', methods=['GET','POST']) 
def index():
    todos = request.form['todos']
    todos.append(todos)
    return render_template("todo.html.jinja", todos = todos)
 