from flask import render_template, Blueprint


home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)

@home_blueprint.route('/')
def hello():
    return render_template('index.html')

@home_blueprint.route('/user/<username>')
def user(username):
    return render_template('user.html', name=username)


@home_blueprint.route('/proper/<age>')
def peopro(age):
    return render_template('proper.html',age=age)