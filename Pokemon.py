class Pokemon:
    def __init__(self,entry,name,types,description,is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught

    def speak(self) :
        return print(f"{self.name} says: {self.description}")

    def display_details(self):
        return print(f"Entry: {self.entry}\nName: {self.name}\nTypes: {self.types}\nDescription: {self.description}\nCaught: {self.is_caught}")
new_pokemon = Pokemon(1,"Bulbasaur","Grass, Poison","A strange seed was planted on its back at birth. The plant sprouts and grows with this Pokémon.",False)
new_pokemon.speak()
new_pokemon.display_details()