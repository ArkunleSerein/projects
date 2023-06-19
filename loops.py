import random
#while : c'est comme un "if" mais qui est répété
while False:
    print("Ce message ne s'affiche pas")



# ctrl+c pour arrêter le programme
# while True:
#    #continue permet de reprendre au début de la boucle suivante.
#    continue
#    print("Ce message est affiché en boucle")
#    #break permet de sortir d'une boucle.
#    break

#_________________________________________________#

#premier tirage
dice = random.randint(1, 6)

while dice !=6:
     print(f"Je n'ai pas tiré un 6, mais un {dice}")
     print("Je recommence un nouveau tirage")
#second tirage
     dice = random.randint(1, 6)
     print(dice)

print("J'ai tiré un 6")

#_________________________________________________#

# recréation de la boucle for classique avec une bouche while
#0 est inclus mais 10 est exclu
i = 0
while i < 10:
     print(f'{i= }')
     i += 1

# boucle à rebours
for i in range(0, -1, -1):
     print(f'{i = }')

#boucle for each
users = ['foo','bar','baz']

for user in users:
     print(user)

# enumerate permet de récupérer l'index de chaque élément
for user in enumerate(users):
     print(f"{i = }, {user = }")

# boucle for $
for i in range(0, len(users)):
     user = users[i]
     print(f"{i = }, {user = }")