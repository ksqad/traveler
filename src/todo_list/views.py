from flask import render_template, Blueprint, jsonify, request, abort, logging

#模拟json数据
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

todo_list_blueprint = Blueprint(
    'todo-list', __name__,
    template_folder='templates'
)


@todo_list_blueprint.route('/todo-list')
def todo_list():
    return render_template('todo-list.html')


@todo_list_blueprint.route('/todo/api/tasks', methods=['GET'])
def getTasks():
    return jsonify({'tasks' : tasks})

@todo_list_blueprint.route('/todo/api/addTask', methods=['POST'])
def add_task():
    if request.json['title'] == "":
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    # tasks变动后返回新数据到页面，状态码201
    return jsonify({'tasks': tasks}), 201

@todo_list_blueprint.route('/todo/api/deleteTask', methods=['POST'])
def delete_task():
    task_id = request.json['id']
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            return jsonify({ 'tasks' : tasks }), 201
    return jsonify({ 'tasks' : tasks })

