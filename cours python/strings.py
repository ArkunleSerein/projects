# déclaration et affectation de chaînes de caractères (strings)

text1 = "lorem"
text2 = "ipsum"

# concaténation

text3 = "citation : " + text1 + " " + text2 +", César"
print(text3)

# interpolation avec une f-string

text3 = f"citation : {text1} {text2}, César"
print(text3)

# attention, la concaténation ne fonctionne qu'avec des STR
# solution, convertir les autres types en STR

mails = 52
text4 = "Vous avez " + str(mails) + " mails non lus"
print(text4)


# La répétition de texte

text5 = "foo" * 3
print(text5)

# Affichage de valeurs arrondies

number1= 10/3
text6 = f"10/3 est à peu près {number1:.2f}"   # ( le (:) permet de faire une conversion (.2f signifie 2 chiffres après la virgule))
print(text6)

# Les fonctions associés aux strings

# (len) permet de connaître la longueur 

text7 = "foo bar baz foo"
print(len(text7))

# (.count) permet de compter le nombre de fois qu'apparait le mot.

print(text7.count('foo'))

# (.find) retrouve l'emplacement d'un mot, ('str',variable + 1 retrouve l'occurence suivante )

position = text7.find('foo')
print(position)
print(text7.find('foo', position + 1))

# si le mot est absent, la fonction renvoie -1

position = text7.find('lorem')
print(position)

# remplacement de mots

text7 = (text7.replace('foo','lorem'))
print(text7)

# split & join

# split joint la chaîne de caractére en liste

list1 = text7.split(' ')
print(list1)

# Join le "" sert à définir par quoi on peut jointer.

text8 = "+" .join(list1)
print(text8)

# pour inverser des mots dans une liste :
#___________________________________________#
# foo = [1, 2, 3]
# tmp = foo[0]
# foo[0], foo[1] = foo[1], foo[0]
#____________________________________________#

