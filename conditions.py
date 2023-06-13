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

# OU exclusif (xor)
print(True ^ False)
print(True ^ False)
print(False ^ True)
print(False ^ False)

# table de vérité de l'opérateur XOR
# A         B           A xor B
# True      True           False 
# True      False          True 
# False     True           True 
# False     False          

# Exo course (opérateur OU logique)
# afficher :
#  - "Je peux aller faire les courses" si on a au moins un moyen de paiement
#  - "Je ne peux pas aller faire les courses" si je n'ai aucun moyen de paiement

has_cash = bool(random.randint(0, 1))
has_cb = bool(random.randint(0, 1))

print(f'{has_cash = }')
print(f'{has_cb = }')

if has_cash == True or has_cb == True: print("Je peux aller faire les courses")
else: print("Je ne peux pas aller faire les courses")

# On peut touver le même résultat avec parce que les varianles sont remplacer par False or True:

if has_cash or has_cb: print("Je peux aller faire les courses")
else: print("Je ne peux pas aller faire les courses")
   

# Exo courses ( opérateur Et logique)

has_cash = bool(random.randint(0, 1))
has_cb = bool(random.randint(0, 1))

print(f'{has_cash = }')
print(f'{has_cb = }')

if  has_cash == False or  has_cb == False: print("Je ne peux pas aller faire les courses")
else: print("Je peux aller faire les courses")

# on retrouve le même résultat avec :

if not has_cash and not has_cb : print("Je ne peux pas aller faire les courses")
else: print("Je peux aller faire les courses")

# combinaison d'opérateurs and et OR 

user_level = 3
user_score = 143
user_credit = 16


    #version bugguée
if user_level >= 3 and user_score >= 100 or user_credit >= 10:
   print("le joueur peut acheter de matériel")
else:
   print("Le joueur ne peut pas acheter de matériel")

   #version corrigé
if (user_level >= 3) and (user_score >= 100 or user_credit >= 10):
   print("le joueur peut acheter de matériel")
else:
   print("Le joueur ne peut pas acheter de matériel")


# exercice carte de réduction
# déterminer la carte de réduction auquelle le voyageur a droit :
#  - entre 0 et 12 ans (inclus), le voyageur a droit à la gratuité
#  - entre 12 et 25 ans (inclus), le voyageur a droit à une réduction de 50 % 
#  - entre 26 et 64 ans (inclus), le voyageur a droit à une réduction de 10 % 
#  - au delà de 65 ans (inclus), le voyageur a droit à une réduction de 50 % 

age = random.randint(0, 99)
print(age)

if age >= 0 and age <= 12 : 
   print("le voyageur a droit à la gratuité")
elif (age >= 12 and age <= 25) or age >=65: 
   print("le voyageur a droit à une réduction de 50 %")
elif age >= 26 and 64 <= 64 : 
   print("le voyageur a droit à une réduction de 10 %")

