# Nombre entier, integer (int)
number1 = 123
number1 = 42
print(number1)

# nombre à virgule flottante, float (float)
number2 = 3.14
number2 = 2.71
print(number2)

# chaine de caractères, string (str)
text1 = 'foo bar baz'
print(text1)

text2 = "foo bar baz"
print(text2)

# booléen, boolean (bool)
python_is_cool = True
print(python_is_cool)

python_is_boring = False
print(python_is_boring)

# valeur nulle, null value (noneType)
user_accepted_terms = None
print(None)

#types de données
print (type(number1))
print (type(number2))
print (type(text1))
print (type(text2))
print (type(python_is_cool))
print (type(python_is_boring))
print (type(user_accepted_terms))

# vérification du type de données
print (type(number1) is int)
print (type(number1) is str)

# to do: intérroger le type des autres variables...

# transtypage int -> str
print(type(str(number1)))
print(str(number1))

# transtypage int-> bool
print(type(bool(number1)))
print(bool(number1))

# convertie en booléen la valeur 0 donne  False
number3 = 0
print((bool(number3)))

#transtypage str -> int génère une erreur
# il ne peut pas y avoir autre chose qu'un nombre
# dans la chaine de caractères 
# si on veut la convertir en int
text3 = "123456789"
print(type(int(text3)))

# les fonctions de transtypage
# str() convertit vers string
# int() convertit vers integer
# float() convertit vers float
# bool ( convertit vers boolean)

# chaîne de caractères, string
# cette notation permet d'utiliser des saut de ligne
text4 = """"<div> <h1>Titre de premier niveau</h1>
</div>
"""

 # \n est équivalent à un saut de ligne
 # \t est équivalent à une tabulation 
text5 = "<div>\n\t<h1>Titre de premier niveau</h1>\n</div>\n"
print(text5)

# la backslash seul est le caractère d'échappement
# \" est équivalent à une guillemet "
# \\ est équivalent à un backslash \

text6 = "foo \"Bar\" Baz"
print(text6)

text7 = "C:\\Program Files\\Foo"
print(text7)

# permuter les 2 variables a et b en utilisant l'opérateur d'affectation et le nom des variables.
a = 123
b = 42
a, b = b, a

print(a,b)

c = 123
d = 42

e = d
d = c
c = e

print( c, d)
# permutation des valeurs de manière arithmétique 

c = b
b = a 
a = c

# permutation de manière pythonique
b, a = a, b

# addition de float
# affiche 0.30000000000000004 au lieu de 0.3
print(0.1 + 0.1 + 0.1)

from decimal import Decimal

# affiche correctement 0.3
print(Decimal("0.1") + Decimal("0.1") + Decimal("0.1"))

# affiche correctement 0.3
print(Decimal ("0.3"))


import decimal
from decimal import Decimal

Decimal('0.1') + Decimal('0.1') + Decimal('0.1') == Decimal('0.3') # True

# demande d'utilisation du mode d'arrondi habituel, c-à-d ROUND_HALF_UP
decimal.getcontext().rounding = decimal.ROUND_HALF_UP
Decimal("0.5").quantize(Decimal("1")) # Decimal('1')
Decimal("1.5").quantize(Decimal("1")) # Decimal('2')


# pour envoyer sur github
# git add 
# git commit
# git push