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

#type hinting
def mult(a: int, b: int) -> int:
    return a * b
    """ Cette fonction ...

    a ...
    b ...
    return ...
    """
result = mult(2, 5)
print(result)
# mais les autres types de données passe quand même
# result = mult('abc', 5)

# le nom de la fonction + ses paramètres + son type de retour = signature de la fonction
# def mult(a: int, b: int) -> int:

#  
#  
#  copie d'une fonction comme ci c'était une variable.
mult_copy = mult
mult_copy(2, 5)

# fonction d'ordre supérieur
# fonction qui accepte une fonction en paramètre ou qui renvoie une fonction
def operateur_binaire(a, b, fonction):
    return fonction(a, b)



# stockage de fonctions dans une liste
operations = []
operations.append(addition)
operations.append(mult)

a = 2
b = 5
resultat = None 

for operation in operations:
    resultat = operation(a, b)
    print(resultat)

# appel de la fonction d'ordre supérieur
resultat = operateur_binaire(2, 5, mult)

my_list = ['foo', 'ipsum']
text = "toto"

print(len(my_list))
print(len(text))

def my_len(value):
    return 42

# Sauvegarde de la fonction len() originale
len_backup = len
# Surcharge de la fonction len() originale (remplacement par une autre fonction)
len = my_len

print(len(my_list))
print(len(text))

# restauration de la fonction len () originale
len = len_backup

# "pass" permet d'écrire du code python syntaxiquement valide même quand on a pas encore le corps ou la condition if ou de la boucle for 
if True:
    pass 

#_________________________________________________________#

""" # fonction RECURSIVE = Fonction qui s'auto-appelle """

#_________________________________________________________#


