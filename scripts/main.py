import json
import sys

import matplotlib.pyplot as plt

from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect

if __name__ == "__main__":
    factory = PokemonFactory("pokemon.json")
    balls = ["pokeball", "ultraball", "fastball", "heavyball"]
    pokemons = ["jolteon", "caterpie", "snorlax", "onix", "mewtwo"]

    # Vamos a intentar atrapar cada pokemon con cada pokeball 100 veces
    catches = {}
    for ball in balls:
        catches[ball] = []
        for pokemon in pokemons:
            poke = factory.create(pokemon, 100, StatusEffect.NONE, 1)
            for _ in range(100):
                catch = attempt_catch(poke, ball, 0.15)
                catches[ball].append(catch[1])

    # Graficamos los resultados
    fig, axs = plt.subplots(2, 2)
    for i, ball in enumerate(balls):
        axs[i // 2, i % 2].hist(catches[ball], bins=400)
        axs[i // 2, i % 2].set_title(ball)

    plt.show()

    # with open(f"{sys.argv[1]}", "r") as f:
    #     config = json.load(f)
    #     ball = config["pokeball"]
    #     pokemon = factory.create(config["pokemon"], 100, StatusEffect.NONE, 1)
    #
    #     # for i in range(100, 1, -1):
    #     #     pokemon = factory.create(config["pokemon"], 100, StatusEffect.NONE, i / 100)
    #     #     print(pokemon.current_hp)
    #
    #     print("No noise: ", attempt_catch(pokemon, ball))
    #     for _ in range(10):
    #         print("Noisy: ", attempt_catch(pokemon, ball, 0.15))
