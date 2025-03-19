import matplotlib.pyplot as plt
import numpy as np

from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect

factory = PokemonFactory("pokemon.json")
pokemons = ["onix", "caterpie"]
healths = ["1", "0.75", "0.5", "0.25", "0.01"]
results = {}

for pokemon_name in pokemons:
    results[pokemon_name] = {}

    for health in healths:
        results[pokemon_name][health] = []
        pokemon = factory.create(pokemon_name, 100, StatusEffect.NONE, float(health))

        for _ in range(100):
            success, _ = attempt_catch(pokemon, "pokeball")
            results[pokemon_name][health].append(success)

# Graficando los resultados
for pokemon, result_data in results.items():
    data = {health: np.mean(r) * 100 for health, r in result_data.items()}

    plt.figure(figsize=(10, 6))
    plt.bar(data.keys(), data.values(), edgecolor="black", color="skyblue")

    plt.xlabel("Porcentaje de vida")
    plt.ylabel("Probabilidad de captura")
    plt.title(f"Efecto de la Vida en la Captura de {pokemon.capitalize()}")

    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.ylim(0, 100)

    for i, rate in enumerate(data.values()):
        plt.text(i, rate, f"{rate:.2f}%", ha="center", va="bottom")

    plt.tight_layout()
    plt.show()
