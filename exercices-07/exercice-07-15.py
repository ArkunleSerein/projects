# exo 7.15
# en utilisant une boucle for, affichez tous les nombres divisibles par 3, de 2 à 99 inclus

# réponse 7.15

for i in range(2, 100):
    if i % 3 == 0:
        print(i, end=" ")