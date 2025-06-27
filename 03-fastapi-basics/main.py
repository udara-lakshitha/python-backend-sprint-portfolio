# 1. Import FastAPI
from fastapi import FastAPI
from pydantic import BaseModel # import BaseModel

# 2. Create an instance of FastAPI class
# This 'App' is the heart of API
app = FastAPI()

# A simple in-memoy database
fake_todo_db = [
    {'id': 1, 'task': 'Learn FastAPI'},
    {'id': 2, 'task': 'Build an API'}
]

# 3. Create a 'path operation decorator'
@app.get('/')
def read_root():
    # 4. The function returns a dictionary, which FastAPI will
    # automatically convert to JSON format
    return {'message': "Welcome to the Monster's First API!"}

# 5. Another endpoint for a different path
@app.get('/status')
def get_status():
    return {'status': 'ok', 'message': 'APi is running smoothly'}

@app.get('/todos')
def get_all_todos():
    return {'todos': fake_todo_db}

@app.get('/todos/{todo_id}')
def get_single_todo(todo_id: int):
    for todo in fake_todo_db:
        if todo['id'] == todo_id:
            return {'todo': todo}
    return {'error': 'Todo not found'}

# Define the data model for a new Todo item
class Todo(BaseModel):
    task: str

@app.post('/todos')
def create_todo(new_todo: Todo): # FastAPI will enforce this model
    # Create a new ID
    new_id = len(fake_todo_db) + 1
    # Create the full todo item dictionary
    todo_item = {'id': new_id, 'task': new_todo.task}
    # Add it to our database
    fake_todo_db.append(todo_item)
    return {'message': 'Todo Created successfully', 'todo': todo_item}