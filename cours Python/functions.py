import library

# définition
def hello():
    print('hello Python!')

# appel ou exécution
hello()

# paramètres
def hello2(name):
    print(f"hello {name}!")

hello2('Foo')

# paramètres + retour de valeur
def addition(a, b):
    return a + b

resultat = addition(42, 123)
print(resultat)

# appel d'une fonction stocker dans un autre module (fichier)
resultat = library. oui_non(False)
print(resultat)
print(library. oui_non(True))

# reverse lookup
my_list = [42, 123, 3.14]

def reverse_lookup(my_list, value):
    """ cette fonction prend en paramètre une liste est une valeur à rechercher. Elle renvoie l'index de la valeur si elle est trouvée ou None si la valeur n'est pas trouvée.
     
      my_list list la list dans laquelle il faut chercher
      value any la valeur à rechercher
      return int si la valeur est trouvée ou None si la valeur n'est pas trouvée 
    """
    for i in range(len(my_list)):
        if my_list[i] == value:
            #@dev
            #print(f'{i = }')
            return i
        
    return None

result = library.reverse_lookup(my_list, 3.14)
print(result)
