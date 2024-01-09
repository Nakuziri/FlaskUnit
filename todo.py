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
        cursor = conn.cursor() 
        new_todos = request.form['new_todos']
        # Todos.append(new_todos)
        cursor.execute(f"INSERT INTO `Todos`(`description`) VALUES ('{new_todos}')")
        conn.commit()
        cursor.close()
    
    cursor = conn.cursor()      
    cursor.execute("SELECT * FROM `Todos`")
    results = cursor.fetchall()
    cursor.close()

    return render_template("todo.html.jinja", new_todos = results)

# @app.route('/delete_todos/<int:todo_index>', methods=['POST'])
# def todo_delete(todo_index):
#     del Todos[todo_index]
#     return redirect('/')