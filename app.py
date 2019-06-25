from flask import Flask, request, render_template, jsonify, redirect

app = Flask(__name__)

todos = ["eat", "sleep", "go home"]

@app.route("/")
def root():
    return redirect("/first")

@app.route("/first")
def first():
    return render_template("first.html")

@app.route("/second")
def second():
    return render_template("second.html")

@app.route("/send-back")
def send_back():
    print("HELLO FROM SERVER!")
    info = request.args["info"]
    return jsonify({'result': info})

@app.route("/todos")
def todo_list():
    return render_template("todo-list.html", todos=todos)

@app.route("/todos/new")
def new_todo():
    return render_template("new-todo-form.html")

@app.route("/todos", methods=["POST"])
def create():
    new_todo = request.form["task"]
    todos.append(new_todo)
    return redirect("/todos")

@app.route("/todos-with-ajax")
def todos_ajax():
    return render_template("todo-list-with-ajax.html")

@app.route("/todos-with-ajax", methods=["POST"])
def create_ajax():
    new_todo = request.json["task"]
    return jsonify({'newTodo': new_todo})