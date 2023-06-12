import random

if True:
    print("Ce message s'affichera toujours")

if False:
    print("Ce message s'affichera jamais")

number1 = random.randint(0, 10)
number2 = random.randint(0, 10)

print(f'{number1 = }')
print(f'{number2 = }')

#block if 1

if number1 < number2:
    print("La variable number1 est plus petite que number2")

#block if 2

if number1 < number2:
    print("La variable number1 est plus petite que number2")  

else: 
    print("La première condition n'est pas vérifiée")

#block if 3

if number1 < number2:
    print("La variable number1 est plus petite que number2")  

else: # number1 >= number2
    print("La variable number1 et plus grande ou égale à number2")

#block if 4

if number1 < number2:
    print("La variable number1 est plus petite que number2")  
else: 
    if number1 > number2:
     print("La variable number1 est plus grande que number2")
    else:
     print("Les deux variables number1 et number2 sont égales")

    # elif == else if

    # opérateurs booléens

# négation
print(not True)
print(not False)

# table de vérité de l'opérateur de négation
# A   Not A
# True, False 
# False True

# OU logique
print(True or True)
print(False or False)
print(True or False)
print(False or True)

# table de vérité de l'opérateur OU logiqiue
# A      B      A or B
#True   True     True
#True   False    True
#False  True     True
#False  False    False

# pour retrouver la table, remplacez :
# - A par "J'ai du cash"
# - B par "j'ai ma CB"
# - "A or B" par "puis-je faire mes courses ?"

# ET logique
print(True and True)
print(False and False)
print(True and False)
print(False and True)

# table de vérité de l'opérateur ET logiqiue
# A      B      A and B
#True   True     True
#True   False    False
#False  True     False
#False  False    False

# table de vérité de l'opérateur NAND ( not and)
# A      B       not (A and B)  A and B
#True   True     False          True
#True   False    True           False            
#False  True     True           False
#False  False    True           False