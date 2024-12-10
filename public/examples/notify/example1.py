
from prune import Prune, notify

class Counter:
    def __init__(self) -> None:
        self.value = 0

    @notify #update the DOM at the end of the method
    def increment(self):
        self.value += 1

    #doesn't update the DOM but the store is still updated
    def decrement(self):
        self.value -= 1

Prune(counter=Counter())