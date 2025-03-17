import json

import matplotlib.pyplot as plt
import numpy as np

from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect

# Configuración del experimento
factory = PokemonFactory("pokemon.json")
pokeballs = ["pokeball", "ultraball", "fastball", "heavyball"]
pokemons = ["jolteon", "caterpie", "snorlax", "onix", "mewtwo"]
results = {}

# Ejecutar simulaciones para cada Pokébola
for pokemon_name in pokemons:
    pokemon = factory.create(pokemon_name, 100, StatusEffect.NONE, 1)
    results[pokemon_name] = {}
    for ball in pokeballs:
        results[pokemon_name][ball] = []
        for _ in range(100):
            _, capture_rate = attempt_catch(pokemon, ball, 0.15)
            results[pokemon_name][ball].append(capture_rate)

# Calcular la probabilidad promedio de captura por Pokébola
average_rates = {pokemon: {ball: np.mean(rates) for ball, rates in pokeball_data.items()} for pokemon, pokeball_data in results.items()}

# Mostrar resultados
print("Probabilidades promedio de captura:")
for pokemon, balls in average_rates.items():
    plt.figure(figsize=(8, 5))
    plt.bar(balls.keys(), balls.values())

    plt.xlabel("Tipo de Pokébola")
    plt.ylabel("Probabilidad de captura")
    plt.title(f"Probabilidad de captura de {pokemon.capitalize()}")

    plt.grid(axis="y", linestyle="--", alpha=0.7)
    # plt.ylim(0, 0.5)

    for i, rate in enumerate(balls.values()):
        plt.text(i, rate, f"{rate:.2f}", ha="center", va="bottom")

    plt.tight_layout()
    plt.show()

    # print(f"\n{pokemon.capitalize()}:")
    # for ball, rate in balls.items():
    #     print(f"{ball.capitalize()}: {rate:.2f}")
