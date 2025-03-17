import matplotlib.pyplot as plt
import numpy as np

from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect

# Configuración del experimento
factory = PokemonFactory("pokemon.json")
pokeballs = ["pokeball", "ultraball", "fastball", "heavyball"]
pokemons = ["jolteon", "caterpie", "snorlax", "onix", "mewtwo"]
results = {}

# Ejecutar simulaciones para cada Pokébola y cada Pokémon
for pokemon_name in pokemons:
    pokemon = factory.create(pokemon_name, 100, StatusEffect.NONE, 1)
    results[pokemon_name] = {b: [] for b in pokeballs}
    for ball in pokeballs:
        for _ in range(100):
            success, _ = attempt_catch(pokemon, ball)
            results[pokemon_name][ball].append(success)

# Calcular la efectividad relativa
effectiveness = {}
for pokemon_name, pokeball_data in results.items():
    pokeball_successes = {ball: sum(attempts) / len(attempts) for ball, attempts in pokeball_data.items()}
    relative_effectiveness = {ball: pokeball_successes[ball] / (pokeball_successes["pokeball"] + 0.000001) for ball in pokeballs}
    effectiveness[pokemon_name] = relative_effectiveness

# Generar gráfico para visualizar los resultados
fig, ax = plt.subplots(figsize=(10, 6))
for pokemon_name, relative_effectiveness in effectiveness.items():
    ax.plot(
        pokeballs,
        [relative_effectiveness[ball] for ball in pokeballs],
        marker="o",
        label=pokemon_name,
    )

# Personalizar el gráfico
ax.set_xlabel("Tipo de Pokébola")
ax.set_ylabel("Efectividad Relativa")
ax.set_title("Efectividad Relativa de las Pokébolas por Pokémon")
ax.legend(title="Pokémon")
ax.grid(axis="y", linestyle="--", alpha=0.7)

# Mostrar el gráfico
plt.tight_layout()
plt.show()
