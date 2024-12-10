
from prune import Prune, notify

class Dropdown:
    def __init__(self) -> None:
        self.visible = False

    @notify
    def toggle(self):
        self.visible = not self.visible

Prune(dropdown=Dropdown())