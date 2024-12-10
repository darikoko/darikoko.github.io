from prune import Prune, notify

class TodoList:
    def __init__(self, tasks:list[str]=["fjd","sdf"]):
        self.tasks = tasks

    @notify
    def add_task(self, task:str):
        self.tasks.append(task) 

Prune(todolist=TodoList())