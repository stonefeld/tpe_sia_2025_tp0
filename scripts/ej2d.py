import json
import numpy as np
from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect

factory = PokemonFactory("pokemon.json")
selected_pokemons = ["caterpie", "snorlax"]
pokeballs = ["pokeball", "ultraball", "fastball", "heavyball"]
levels = [10, 25, 50, 75, 100]
hp_percentages = [0.1, 0.25, 0.5, 0.75, 1.0]
status_effects = [StatusEffect.NONE, StatusEffect.PARALYSIS, StatusEffect.SLEEP, StatusEffect.FREEZE]

results = []

for level in levels:
    for hp in hp_percentages:
        for status in status_effects:
            for ball in pokeballs:
                capture_probabilities = {}
                
                for pokemon_name in selected_pokemons:
                    pokemon = factory.create(pokemon_name, level, status, hp)
                    rates = [attempt_catch(pokemon, ball, 0.15)[1] for _ in range(100)]
                    capture_probabilities[pokemon_name] = round(np.mean(rates), 2)
                
                results.append({
                    "Level": level,
                    "HP%": int(hp * 100),
                    "Status": status.name,
                    "Pokeball": ball,
                    **{f"Capture Probability {pokemon}": prob for pokemon, prob in capture_probabilities.items()}
                })

# Determinar las mejores combinaciones generales
best_combinations = []
best_probability = 0

for combination in results:
    avg_prob = np.mean([combination[f"Capture Probability {pokemon}"] for pokemon in selected_pokemons])
    
    if avg_prob > best_probability:
        best_probability = avg_prob
        best_combinations = [combination]
    elif avg_prob == best_probability:
        best_combinations.append(combination)

print("Mejores combinaciones para capturar ambos Pokémon:")
for comb in best_combinations:
    print("-")
    for key, value in comb.items():
        print(f"{key}: {value}")
