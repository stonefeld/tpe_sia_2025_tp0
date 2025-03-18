import json
import matplotlib.pyplot as plt
import numpy as np

from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect

factory = PokemonFactory("pokemon.json")
pokeball = "pokeball"  # Solo usaremos la Pokébola básica
pokemons = ["jolteon", "caterpie", "snorlax", "onix", "mewtwo"]
status_effects = [
    StatusEffect.NONE, StatusEffect.POISON, StatusEffect.BURN, 
    StatusEffect.PARALYSIS, StatusEffect.SLEEP, StatusEffect.FREEZE
]
results = {}


for pokemon_name in pokemons:
    
    results[pokemon_name] = {}

    for status in status_effects:
        results[pokemon_name][status.name] = []

        for _ in range(100): 
            pokemon = factory.create(pokemon_name, 100, status, 1)  
            _, capture_rate = attempt_catch(pokemon, pokeball, 0.15)
            results[pokemon_name][status.name].append(capture_rate)


average_rates = {
    pokemon: {
        status: np.mean(rates) for status, rates in status_data.items()
    } for pokemon, status_data in results.items()
}


for pokemon, status_data in average_rates.items():
    plt.figure(figsize=(10, 6))

    plt.bar(status_data.keys(), status_data.values(), color=["red", "orange", "yellow", "blue", "purple", "cyan"])

    plt.xlabel("Estado de Salud")
    plt.ylabel("Probabilidad de Captura")
    plt.title(f"Efecto del Estado de Salud en la Captura de {pokemon.capitalize()}")

    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.ylim(0, 1)

    for i, (status, rate) in enumerate(status_data.items()):
        plt.text(i, rate, f"{rate:.2f}", ha="center", va="bottom")

    plt.tight_layout()
    plt.show()
