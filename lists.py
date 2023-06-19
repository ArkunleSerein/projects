empty_list = []
users = ['foo','bar','baz']
mix = [True, 3.14,'lorem ipsum', None, [123,42]]

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

#ajouter un nouvel élément au début ou au milieu.
users.insert(0,'sit')
users.insert(2,'dolores')
print(users)