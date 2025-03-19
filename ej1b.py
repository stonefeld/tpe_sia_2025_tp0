import json
import matplotlib.pyplot as plt
import numpy as np
from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect

factory = PokemonFactory("pokemon.json")
pokemon_names = ["jolteon", "caterpie", "snorlax", "onix", "mewtwo"]
pokeballs = ["pokeball", "ultraball", "fastball", "heavyball"]

results = {pokemon: {ball: 0 for ball in pokeballs} for pokemon in pokemon_names}

for pokemon_name in pokemon_names:
    for ball in pokeballs:
        pokemon = factory.create(pokemon_name, 50, StatusEffect.NONE, 1.0)
        rates = [attempt_catch(pokemon, ball, 0.15)[1] for _ in range(1000)]
        results[pokemon_name][ball] = np.mean(rates)
    
relative_effectiveness = {}
    
for pokemon in pokemon_names:
    pokeball_success = results[pokemon]["pokeball"] 
    relative_effectiveness[pokemon] = {ball: results[pokemon][ball] / pokeball_success for ball in pokeballs}

plt.figure(figsize=(10, 6))
for pokemon, effectiveness in relative_effectiveness.items():
    plt.plot(pokeballs, list(effectiveness.values()), marker='o', label=pokemon)

plt.xlabel("Tipo de Pokébola")
plt.ylabel("Efectividad Relativa")
plt.title("Efectividad Relativa de las Pokébolas por Pokémon")
plt.legend(title="Pokémon")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()