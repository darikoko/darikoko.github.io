from prune import Prune, notify

class Bob:
    def __init__(self):
        self.rotate = False
        self.scale = 1

    @notify
    def toggle_rotate(self):
        self.rotate = not self.rotate

    @notify
    def update_scale(self, new_scale:int):
        self.scale = new_scale
    


Prune(bob=Bob())