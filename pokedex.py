from lista import List

#Testando lista

pokedex = List()

with open("pokemon.csv", "r+") as pokelista:

    skip = True
    for pokemon in pokelista:
        if skip:
            skip = False
            continue
        pokedex.append(*pokemon.split(","))

print(pokedex)