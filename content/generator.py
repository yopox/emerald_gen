import json
import random


class ContentGenerator():
    """Loads all items and pokemon."""

    def __init__(self):
        self.types = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice",
                      "Fighting", "Poison", "Ground", "Flying", "Psychic",
                      "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel"]
        with open("content/pokemon.json") as poke_json:
            self.pokemon = json.load(poke_json)
        with open("content/items.json") as item_json:
            self.items = json.load(item_json)

    def getRandomPokemon(self, n, weights=None):
        """Returns n random pokemon."""
        return random.choices(self.pokemon, weights, k=n)

    def getRandomPokemonOfType(self, type, n, weights=None):
        """Returns n random pokemon of given type."""
        subPoke = [p for p in self.pokemon if type in p['type']]
        return random.choices(subPoke, weights, k=n)

    def getRandomItem(self, n, weights=None):
        """Returns n random items."""
        return random.choices(self.items, weights, k=n)