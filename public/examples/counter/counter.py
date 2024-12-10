from prune import Prune, notify #we need to import prune stuff

class Counter:
    def __init__(self):
        self.value = 0

    @notify #functions decorated by notify will trigger a new render in the DOM
    def increment(self):
        self.value += 1

    @notify 
    def decrement(self):
        self.value -= 1

    @notify 
    def reset(self):
        self.value = 0


#prune instanciation gives access to a global store
#from anywhere in the HTML.
Prune(counter=Counter())