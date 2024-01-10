from flask import Flask, render_template, request, redirect
import pymysql 
import pymysql.cursors
from pprint import pprint as print

conn = pymysql.connect(
   database="xcampos_todos",
   user='xcampos',
   password='221349988',
   host='10.100.33.60', 
   cursorclass=pymysql.cursors.DictCursor
)

app = Flask(__name__)

# Todos = ["Hang out with friend", "Play on my computer"]

@app.route('/', methods=['GET','POST']) 
def index():
    if request.method == "POST" :
        new_todos = request.form['new_todos']
        cursor = conn.cursor()
        # Todos.append(new_todos)
        cursor.execute(f"INSERT INTO `Todos`(`description`) VALUES ('{new_todos}')")
        cursor.close()
        conn.commit()

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `Todos` ORDER BY `complete`")      
    cursor.execute("SELECT * FROM `Todos`")
    results = cursor.fetchall()
    cursor.close()

    return render_template("todo.html.jinja", new_todos = results)

@app.route('/delete_todos/<int:todo_index>', methods = ['POST'])
def todo_delete(todo_index):
    cursor=conn.cursor()
    cursor.execute(f"DELETE FROM `Todos` WHERE `id` = {todo_index}")
    cursor.close()
    conn.commit()
    return redirect('/')

@app.route('/complete_todo/<int:todo_index>', methods = ['POST'])
def todo_complete(todo_index):
    cursor = conn.cursor()
    cursor.execute(f"UPDATE `Todos` SET `complete` = 1 WHERE `id` = {todo_index}")
    cursor.close()
    conn.commit()
    return redirect('/')
