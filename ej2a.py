import matplotlib.pyplot as plt
import numpy as np

from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect

factory = PokemonFactory("pokemon.json")
pokeball = "pokeball"
pokemons = ["onix", "caterpie"]
effects = [StatusEffect.NONE, StatusEffect.POISON, StatusEffect.BURN, StatusEffect.PARALYSIS, StatusEffect.SLEEP, StatusEffect.FREEZE]
results = {}

for pokemon_name in pokemons:
    results[pokemon_name] = {}

    for effect in effects:
        results[pokemon_name][effect.name] = []
        pokemon = factory.create(pokemon_name, 100, effect, 1)

        for _ in range(100):
            success, _ = attempt_catch(pokemon, pokeball, 0.15)
            results[pokemon_name][effect.name].append(success)


for pokemon, result_data in results.items():
    data = {effect: np.mean(r) * 100 for effect, r in result_data.items()}

    plt.figure(figsize=(10, 6))
    plt.bar(data.keys(), data.values(), edgecolor="black", color="skyblue")

    plt.xlabel("Estado de Salud")
    plt.ylabel("Probabilidad de Captura")
    plt.title(f"Efecto del Estado de Salud en la Captura de {pokemon.capitalize()}")

    plt.grid(axis="y", linestyle="--", alpha=0.7)
    # plt.ylim(0, 1)

    for i, rate in enumerate(data.values()):
        plt.text(i, rate, f"{rate:.2f}%", ha="center", va="bottom")

    plt.tight_layout()
    plt.show()
