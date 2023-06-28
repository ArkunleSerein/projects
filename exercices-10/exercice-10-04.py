# exo 10.4
# Créer une fonction nommée `is_greater()` qui :
# - prend deux paramètres `a` et `b` de type `float`
# - renvoie une valeur booléenne
# - renvoie True si `a` est plus grand que `b`
# - renvoie False dans les autres cas
# Appelez la fonction et affichez le résultat

# réponse 10.4

import random

a = random.randint(1, 10)
b = random.randint(1, 10)
print(a, b)


def is_greater(a: float, b: float) -> bool:
        if a > b:
            return True
        else: 
            return False

result = a > b
print(result)