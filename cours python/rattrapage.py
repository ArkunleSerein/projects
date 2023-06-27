import random
users = ['foo', 'bar','baz']

   # boucle for classique

# cette boucle est la même que celle de JS 
# for (let i = 0, i < n; i++) {}

for i in range(len(users)):
    print(i,users[i])

# boucle for classique avec un pas de 2 (step)
# seule cette boucle permet de sauter des éléments dans une liste 

for i in range(0, len(users), 2):
    print(i, users[i])

   # boucle for each

for user in users:
    print(user)

   # boucle for each avec enumerate

# équivalent fonctionnel de la for classique mais préférée par les codeurs python

for i, user in enumerate(users):
    print(i, user)

# pour toute opération on peut utiliser chacune des boucles
# si on veux un index on peut utiliser uniquement la boucle for et foreach enumerate

   # une boucle while

while True:
    r = random.randint(1,100)
    print(r,end=" ")
    if r == 100:
        break

# équivalent fonctionnel de la for while mais celle du dessus est préférée par les codeurs python

r = random.randint(1,100)
print(r,end=" ")

while r != 100:
    r = random.randint(1,100)
    print(r, end=" ")

# ________________________________________________________________________________________________________#

   # str

text1 = 'foo bar baz foo bar baz foo bar baz foo'

for i, char in enumerate(text1):
    print(i, char)

print(text1.find('bar'))
print(text1.find('Bar'))
position = text1.find('foo')
print(position)
print(text1.find('foo', position + 1))

#
# ________________________________________________________________________________________________________#

keyword = 'foo'
position = -1
count = 0

while True:
    position = text1.find(keyword, position + 1)
    print(position)

    if position != -1:
        # pas trouvé
        break
    else: 
        # trouvé
        count += 1

print(count)
print(text1.count('foo'))



   # code ASCII d'un caractère 

print(ord('A'))
print(ord('a'))

   # récupérer un caractère à partir de son code ASCII

print(chr(65))
print(chr(97))

text2 = "lorem ipsum"

# Affiche le iéme caractère du str
print(text2[1])

# Affiche les caractères de l'index 1 inclus à l'index 7 exclus (C-à-D) jusqu'à 6 inclus
print(text2[1:7])

# Affiche un caractère sur deux, de l'index 1 inclus à l'index 7 exclus (C-à-D jusqu'à 6 inclus)
print(text2[1:7:2])

# Affiche à rebours (-1) les caractères de l'index 6 inclus à l'index 0 exclus (C-à-D jusqu'à 1 inclus)
print(text2[6:0:-1])

# syntaxe
# str [start:end:step]
# ATTENTION: end est exclue



text3 = 'foo bar baz'
text3_list = text3.split('bar')
print(text3_list)
text3 = 'lorem'.join(text3_list)
print(text3)


   # Algorithme récursives récursives VS algorithmes itératifs

# suite de fibonacci 

# index:  0 1 2 3 4 5 6 7  8  9
# valeur: 0 1 1 2 3 5 8 13 21 34 ...
# f(n) = f(n-1) + f(n - 2)


# exemple :
# f(9) = f(8) + f(7)
# 34   = 21   + 13

memo = {
    0: 0,
    1: 1
}

def fibonacci(n):
# si le résultat est déjà dans le mémo on renvoie le résultat
    if n in memo:
        return memo[n]
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        #on calcul le résultat
        result = fibonacci(n-1) + fibonacci(n - 2)
        # on stock le résultat dans le mémo
        memo[n] = result
        return result
    
print(fibonacci (0))
print(fibonacci (1))
print(fibonacci (300))
