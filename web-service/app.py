from flask import Flask,render_template
from flask_restful import reqparse, abort, Api, Resource
from home import *
from tag_api import *
app = Flask(__name__)
api = Api(app)

"""
PROSSIMI STEP DA FARE:
-DIVIDERE IL COMPORTAMENTO DEL TEMPLATE DEL PRIMO TAB
-IMPLEMENTARE IL COMPORTAMENTO DEL TAB2SELEZIONARE COMPONENTS SINGOLI PER OTTENERE LIBRERIE
- TAB STATEMENTS
-TAB OVERVIEW DEVE CONTENERE TUTTE LE COMPONENTI E LIBRERIE SELEZIONATE
-SALVATaggio del codice
"""


TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')



class Home(Resource):
    @app.route('/')
    @app.route('/tag/<tag>')
    def index(name=None,tag=None,components=None):
        name='ReSyDuo'
        if tag:
            components = Get_component_by_tag.get(tag)
        tag_list = ['tag1','tag5','tag3','tag4']
        return render_template('index.html', name=name,tag_list=tag_list,components=components)

# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201




# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')


if __name__ == '__main__':
    app.run(debug=True)