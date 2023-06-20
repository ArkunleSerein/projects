# exo 6.17
# Affichez la valeur qui se trouve à la colonne 4, ligne 3
#
# ATTENTION : faire `- 1` pour obtenir les index correspondant
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

import random

size = 5
matrix = []

for _ in range(0, size):
    row = [random.randint(40, 100) for _ in range(0, size)]
    matrix.append(row)

print(matrix)

# réponse 6.17

row_index = 2
col_index = 3

value = matrix[row_index][col_index]
print("La valeur à la colonne", col_index+1, "ligne", row_index+1, "est :", value)