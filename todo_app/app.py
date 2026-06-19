
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Initialize the todo list
todos = []

# Define a function to add a new todo item
def add_todo(title, description):
    todos.append({'title': title, 'description': description})
    return {'message': 'Todo added successfully'}

# Define a function to get all todo items
def get_all_todos():
    return [{'title': todo['title'], 'description': todo['description']} for todo in todos]

# Define a function to update a todo item
def update_todo(title, new_title=None, new_description=None):
    for todo in todos:
        if todo['title'] == title:
            if new_title:
                todo['title'] = new_title
            if new_description:
                todo['description'] = new_description
            return {'message': 'Todo updated successfully'}
    return {'message': 'Todo not found'}

# Define a function to delete a todo item
def delete_todo(title):
    for i, todo in enumerate(todos):
        if todo['title'] == title:
            del todos[i]
            return {'message': 'Todo deleted successfully'}
    return {'message': 'Todo not found'}

@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.json
    if 'title' not in data or 'description' not in data:
        return jsonify({'message': 'Missing title or description'}), 400
    return add_todo(data['title'], data['description'])

@app.route('/todos', methods=['GET'])
def get_all_todos():
    return jsonify(get_all_todos())

@app.route('/todos/<string:title>', methods=['PUT'])
def update_todo_(title):
    data = request.json
    if 'new_title' in data:
        new_title = data.get('new_title')
    else:
        new_title = None

    if 'new_description' in data:
        new_description = data.get('new_description')
    else:
        new_description = None

    return update_todo(title, new_title or None, new_description or None)

@app.route('/todos/<string:title>', methods=['DELETE'])
def delete_todo_(title):
    return jsonify(delete_todo(title))

if __name__ == '__main__':
    app.run(debug=True)
```

```markdown
#