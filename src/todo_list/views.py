from flask import render_template, Blueprint, jsonify, request, abort, logging

from src import db
from src.models import Tasks

todo_list_blueprint = Blueprint(
    'todo-list', __name__,
    template_folder='templates'
)


@todo_list_blueprint.route('/todo-list')
def todo_list():
    return render_template('todo-list.html')

@todo_list_blueprint.route('/todo/api/tasks', methods=['GET'])
def getTasks():
    tasks = Tasks.query.all()
    return jsonify(tasks=[i.serialize for i in tasks])

@todo_list_blueprint.route('/todo/api/addTask', methods=['POST'])
def add_task():
    if request.json['title'] == "":
        abort(400)

    title = request.json['title']
    description = request.json.get('description', "")
    task = Tasks(title=title, description=description, done=False)
    db.session.add(task)
    db.session.commit()
    tasks = Tasks.query.all()
    # tasks变动后返回新数据到页面，状态码201
    return jsonify(tasks=[i.serialize for i in tasks]), 201

@todo_list_blueprint.route('/todo/api/deleteTask', methods=['POST'])
def delete_task():
    id = request.json['id']
    task = Tasks.query.get(id)
    db.session.delete(task)
    db.session.commit()
    tasks = Tasks.query.all()
    # tasks变动后返回新数据到页面，状态码201
    return jsonify(tasks=[i.serialize for i in tasks]), 201

