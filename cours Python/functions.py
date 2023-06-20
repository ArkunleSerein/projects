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