from random import randrange
from prune import Prune, notify_async, notify
from pyscript import fetch

class Pokedex:

    def __init__(self):
        self.pokemon = None
        self.loading = False

    @notify
    def toggle_loading(self):
        self.loading = not self.loading

    @notify_async #update the DOM at the end of the method
    async def get_random_pokemon(self):
        self.toggle_loading()
        pokemon_id = randrange(1,100)
        response = await fetch(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
        data = await response.json()
        self.pokemon = data
        self.toggle_loading()

Prune(pokedex=Pokedex())