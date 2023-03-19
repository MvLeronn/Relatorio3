from database import Database
from save_json import writeAJson

db = Database(database="dex", collection="pokemons")
db.resetDatabase()
pokemons = db.collection.find()
pokemons = db.collection.find()
for pokemon in pokemons: #printando ela
    print(pokemon)

def getPokemonByDex(number: int):
    return db.collection.find({"id": number})


bulbasaur = getPokemonByDex(1)
writeAJson(bulbasaur, "bulbasaur")

pokemon = db.collection.find({"type": "Grass", "base.Attack": { "$lte": 40 }})
writeAJson(pokemon, "pokemon_grass")

pokemon = db.collection.find({"type": "Fire", "base.Attack": { "$gte": 40 }})
writeAJson(pokemon, "pokemon_fire")

def get_seteletrasmenos(collection):
  names = collection.find({}, {"name": 1})
  seteletrasmenos = []
  for name in names:
    if len(name["name"].keys()) <= 7:
      if all(len(word) <= 7 for word in name["name"].values()):
        seteletrasmenos.append(name["name"].values())
  return seteletrasmenos

writeAJson(get_seteletrasmenos(db.collection), "pokemon_7letrasmenos")

pokemon = db.collection.find({"type": "Water"})
writeAJson(pokemon, "pokemon_water")