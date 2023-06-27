#________________________________________________________________________________________#

                    # scope (étendue)= portée des variables #

#________________________________________________________________________________________#

my_var = 123

def my_func1():
    print(my_var)
    print(my_var2)

my_var2 = 42

# la fonction voit les variables définies à l'extérieur au préalable ou à postériori

my_func1()

#________________________________________________________________________________________#

def my_funct1():
    my_var3 = 3.14

# my_func2()

# il n'est pas possible d'accéder à une variable définie à l'intérieur d'une fonction, que celle-ci est était executée ou non
# principe du verre tinté (comme une limousine)
# NameError: name 'my_var3' is not defined. Did you mean: 'my_var'?

# print(my_var3)

#________________________________________________________________________________________#

my_var4 = 'foo'

def my_func3(my_var4):

    # le paramètre my_var4 masque la variable définie à l'extérieur de la fonction 

    print(my_var4)

# cet appel affiche 'bar'

my_func3('bar')

#________________________________________________________________________________________#

my_var4 = 'foo'

def my_func4():
    # la variable de my_var4 fait de l'ombre à la variable définie à l'extérieur de la fonction 
    my_var4 = 'baz'
    print(my_var4)

my_func4()

# la variable de my_var4 définie à l'extérieur de la fonction reste inchangée

print(my_var4)

#________________________________________________________________________________________#

def my_func5(myvar5):
    my_var5 = 'foo'

my_var6 = 123

# les variables de types int, float, bool ou str sont passés par valeur
# c-à-d que la fonction pourra accéder à la variable originale définie à l'extérieur

my_func5(my_var6)
print(my_var6)

#________________________________________________________________________________________#

def my_func6(my_var7: list):
    my_var7.append('foo')

my_var8 = [123, 42, 3.14]

# les variables de types list, dict, tuple ou objet sont passées par référence
# c-à-d que la fonction pourra accéder à la variable originale définie à l'extérieur

my_func6(my_var8)
print(my_var8)

#________________________________________________________________________________________#