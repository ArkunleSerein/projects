# exo 6.15
# Trouvez la chaîne de caractères la plus longue dans une liste.
# Affichez son index, sa valeur et sa longueur.
#
# ATTENTION : ne pas utiliser la fonction list.index()
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']

# réponse 6.15
longest_string = ''
longest_length = 0
longest_index = -1

for index, string in enumerate(my_list):
    if len(string) > longest_length:
        longest_string = string
        longest_length = len(string)
        longest_index = index

print("Index:", longest_index)
print("Valeur:", longest_string)
print("Longueur:", longest_length)