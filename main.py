from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel

app = FastAPI()

class TodoItem(BaseModel):
    text: str
    done: bool


todos = {}

#Search for a task
@app.get("/todos/{todo_id}")
def read_todo(todo_id: int = Path(None, description="the ID of the task you want to look for:", gt=0)):
    if todo_id not in todos:
        return {"Task Not Found"}
    return todos[todo_id]

#Make a task
@app.post("/todos")
def create_todo(todo: TodoItem):
    todo_id = len(todos) + 1
    todos[todo_id] = todo
    return {"id": todo_id}

#Edit a task
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: TodoItem):
    if todo_id not in todos:
        return {"Task Not Found"}
    todos[todo_id] = todo
    return todos[todo_id]

#Delete a Task
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    if todo_id not in todos:
        return {"Task Not Found"}
    del todos[todo_id]
    return {"message": "Task deleted"}


