
from prune import Prune, notify

class Editor:
    def __init__(self) -> None:
        self.editable = True

    @notify #update the DOM at the end of the method
    def toggle_editable(self):
        self.editable = not self.editable

Prune(editor=Editor())