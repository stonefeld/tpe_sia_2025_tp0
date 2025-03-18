import json
import matplotlib.pyplot as plt
import numpy as np
from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect

factory = PokemonFactory("pokemon.json")
selected_pokemon = "caterpie"
pokeball = "pokeball"

levels = [10, 25, 50, 75, 100]
hp_percentages = [0.1, 0.25, 0.5, 0.75, 1.0]
status_effects = [StatusEffect.NONE, StatusEffect.PARALYSIS, StatusEffect.SLEEP, StatusEffect.FREEZE]

results = {"Level": {}, "HP%": {}, "Status": {}}

for level in levels:
    pokemon = factory.create(selected_pokemon, level, StatusEffect.NONE, 1.0)
    rates = [attempt_catch(pokemon, pokeball, 0.15)[1] for _ in range(100)]
    results["Level"][str(level)] = np.mean(rates)

for hp in hp_percentages:
    pokemon = factory.create(selected_pokemon, 50, StatusEffect.NONE, hp)
    rates = [attempt_catch(pokemon, pokeball, 0.15)[1] for _ in range(100)]
    results["HP%"][f"{int(hp * 100)}%"] = np.mean(rates)

for status in status_effects:
    pokemon = factory.create(selected_pokemon, 50, status, 1.0)
    rates = [attempt_catch(pokemon, pokeball, 0.15)[1] for _ in range(100)]
    results["Status"][status.name] = np.mean(rates)

for param, data in results.items():
    plt.figure(figsize=(8, 5))
    plt.bar(data.keys(), data.values(), color='royalblue', alpha=0.7, edgecolor='black')
    plt.xlabel(param)
    plt.ylabel("Probabilidad de captura")
    plt.title(f"Impacto de {param} en la captura de {selected_pokemon.capitalize()}")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.xticks(rotation=0)
    for i, (key, rate) in enumerate(zip(data.keys(), data.values())):
        plt.text(i, rate, f"{rate:.2f}", ha="center", va="bottom")
    plt.tight_layout()
    plt.show()

print("Resultados del análisis:")
for param, data in results.items():
    print(f"\n{param}:")
    for key, value in data.items():
        print(f"{key}: {value:.4f}")
