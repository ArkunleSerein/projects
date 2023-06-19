empty_list = []
users = ['foo','bar','baz']
mix = [True, 3.14,'lorem ipsum', None, [123,42]]

# il faut préférer cette présentation de liste quand il plusieurs liste dans une list.

mix = [
        True,
        3.14,
        'lorem ipsum',
        None,
        [123,42]
]

# 0 est l'index du premier élément

print(users[0])

# len -1 est l'index du dernier élément

i = len(users) - 1
print(users[i])

# l'index dépasse la taille de la liste
# print(users[100 + 42 - i]) IndexError: list index out of range

# accés en écriture

users[0] = 'lorem'

####### VARIABLE SCALAIRE = VARIABLE QUI INDIQUE UNE ECHELLE #######

# ajouter un nouvel élement

users.append('ipsum')

print(users)

# ajouter un nouvel élément au début ou au milieu.

users.insert(0,'sit')
users.insert(2,'dolores')
print(users)

# enlever un élément d'une list 

last_user = users.pop()
print(last_user, users)

# retrait du dernier élément

last_user = users.pop()
print(last_user)

# retrait par index

first_user = users.pop(0)
print(first_user)
print(users)

# suppression par valeur

users.remove('bar')
print(users)


fruits = ['ananas','banane', 'cerise']
legumes = ['artichaud', 'brocoli', 'carotte']
ingredients = fruits + legumes
print(ingredients)

fruits += legumes
print(fruits)

letters = ['g','d', 'a', 'c','b','Z']
letters = sorted(letters)
print(letters)

# ______________________list 2D
players = [
    [42000, 46400, 32103],
    [16700, 44000, 57987],
]

line = 0
col = 0
print(players[line][col])

for line_index in range(0, len(players)):
        line = players[line_index]

        for col_index in range(0, len(line)):
                score = line[col_index]

                print(score)
