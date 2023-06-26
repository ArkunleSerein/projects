# exo 7.10
# en utilisant une boucle for, on tire 100 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# utilisez une variable compteur `count` pour compter le nombre de fois où `r` est plus grand ou égal à 7
# affichez la variable `count` après la boucle

import random

# réponse 7.10

count = 0

for _ in range(100):
    r = random.randint(1, 10)
    print(r, end=" ")
    if r >= 7:
        count += 1

        
print( " \n count = ", count)