import random

# Paramètres
n_mesures = 60
tension_initiale = random.uniform(0, 500)  # Première valeur aléatoire dans la plage
variation_max = 0.12  # 12%

# Génération des mesures avec variation de ±12% par rapport à la valeur précédente
mesures_tension = [tension_initiale]

for _ in range(n_mesures - 1):
    variation = random.uniform(1 - variation_max, 1 + variation_max)
    nouvelle_valeur = mesures_tension[-1] * variation
    mesures_tension.append(round(nouvelle_valeur, 2))

# Formatage en chaîne avec séparateur ";"
mesures_tension_str = "[" + ";".join(map(str, mesures_tension)) + "]"

print(mesures_tension_str)
