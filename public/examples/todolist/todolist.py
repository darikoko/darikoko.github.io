from prune import Prune, notify #we need to import prune stuff

class Task:
    def __init__(self, text:str):
        self.text = text
        self.done = False

    @notify #functions decorated by notify will trigger a new render in the DOM
    def toggle_done(self):
        self.done = not self.done

class TodoList:
    def __init__(self, tasks:list(Task)=[]):
        self.tasks = tasks

    @notify
    def add_task(self, task:Task):
        self.tasks.append(task)

    @notify
    def remove_task(self, index:int):
        del self.tasks[index]

#prune instanciation gives access to a global store
#from anywhere in the HTML.
Prune(todolist=TodoList(), global_scope=globals())