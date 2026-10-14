import sys
import os
import json
from datetime import datetime


def represent_task(task: object):
    """
    Equivalent of a class __str__ function, this makes task representation in the console way easier.
    """
    id = task['id']
    description = task['description']
    status = task['status']
    createdAt = task['createdAt']
    updatedAt = task['updatedAt']
    print(f"Task id: {id}, description: {description}, currently: {status}, was created at: {createdAt} and updated at: {updatedAt}")


def add_task(description: str):
    task_list = load_tasks()
    max_id = max([t['id'] for t in task_list], default=0)
    task_id = max_id + 1
    task_status = "todo"
    createdAt = datetime.now().isoformat()
    updatedAt = datetime.now().isoformat()

    task_object = {
        "id": task_id,
        "description": description,
        "status": task_status,
        "createdAt" : createdAt,
        "updatedAt": updatedAt
    }

    task_list.append(task_object)
    save_tasks(task_list)
    print(f"Task added succesfully (ID: {str(task_id)}, description: {description})")

def update_task(id:str, new_description: str):
    task_list = load_tasks()
    for t in task_list:
        if id==str(t['id']):
            t['description'] = new_description
            t['updatedAt'] = datetime.now().isoformat()
    
    save_tasks(task_list)


def delete_task(id: str):
    """
    Computes a new list with all the elements EXCEPT the element corresponding the ID, so it gets deleted. Uses List Comprehension
    """
    task_list = load_tasks()
    new_list = [t for t in task_list if str(t['id'])!=id]
    if len(new_list) == len(task_list):
        print("ID not found!")
        return

    print(f"Deleted task {id}!")
    save_tasks(new_list)
    


def list_tasks(query: str): 
    """
    Lists all of the existent tasks in the console, in a parsed form, created in represent_task()
    """
    task_list = load_tasks()
    if query in [None,""," ",'']:
        for t in task_list:
            represent_task(t)
    elif query == "done":
        for t in task_list:
                if t['status']=="done":
                  represent_task(t)
    elif query == "todo":
        for t in task_list:
                if t['status']=="todo":
                    represent_task(t)
    elif query == "in-progress":
        for t in task_list:
                if t['status']=="in-progress":
                    represent_task(t)

def mark_status(new_status:str, id: str):
    """
    Marks a status as in progress or done, then updates the task_list json using save_tasks()
    """
    if new_status not in ["done", "todo", "in-progress"]:
        print("Invalid status name!")
        return

    task_list = load_tasks()
    for t in task_list:
        if id==str(t['id']):
            t['status'] = new_status
            t['updatedAt'] = datetime.now().isoformat()

    save_tasks(task_list)


def load_tasks():
    try:
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as file:
                return json.load(file)
    except json.JSONDecodeError:
        return []



    
def save_tasks(tasks):
        try:
            file = open("tasks.json", "w")
            json.dump(tasks, file, indent=3)
        except OSError as e:
            raise e
""""
CLI hierarchy:
arg[0] -> command name
args[1] -> command
args[2] -> real arg, in this project scope it's id
"""


if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        command = args[1]
        if command=="list":
            list_tasks(None)
        if len(args) > 2:
            body = args[2]
            if(command=="add"):
                add_task(body)
            elif command=="update":
                update_task(body, args[3])
            elif command=="delete":
                delete_task(body)
            elif command=="mark":
                mark_status(body, args[3])
            elif command == "list":
                list_tasks(body)
        else:
            sys.exit()