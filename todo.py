from flask import Flask, render_template, request, redirect
import pymysql 
import pymysql.cursors

conn = pymysql.connect(
   database="xcampos_todos",
   user='xcampos',
   password='221349988',
   host='10.100.33.60', 
   cursorclass=pymysql.cursors.DictCursor
)

app = Flask(__name__)

todos = ["Hang out with friend", "Play on my computer"]

@app.route('/', methods=['GET','POST']) 
def index():
    if request.method == "POST" :
        new_todos = request.form['todos']
        cursor = conn.cursor()
        cursor.execute("SELECT `description` FROM `todos`")
        results = cursor.fetchall()
        if request.method == "POST":
            new_todos = request.form[todos]
            todos.append(new_todos)
    return render_template("todo.html.jinja", new_todos = todos)

@app.route('/delete_todos/<int:todo_index>', methods=['POST'])
def todo_dalete(todo_index):
    del todos[todo_index]
    return redirect('/')