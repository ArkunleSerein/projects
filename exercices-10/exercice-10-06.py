# exo 10.6
# La formule suivante permet de convertir des mètres en miles :
#
#       miles = meters / 1609.344
#
# La formule suivante permet de faire l'inverse :
#
#       meters = miles * 1609.344
#
# Créez une fonction nommée :
#
# - meters_to_miles() permettant de convertir des mètres en miles
# - miles_to_meters() permettant de convertir des miles en mètres
#
# Ensuite convertissez les valeurs :
#
# - 1 Km en miles
# - 10 miles en mètres
#
# Appelez les fonctions et affichez les résultats

# réponse 10.6

def meters_to_miles(meters):
    miles = meters / 1609.344
    return miles

def miles_to_meters(miles):
    meters = miles * 1609.344
    return meters

# Conversion de 1 kilomètre en miles
km = 1
miles = meters_to_miles(km * 1000)
print(f"{km} km est égal à {miles} miles.")

# Conversion de 10 miles en mètres
miles = 10
meters = miles_to_meters(miles)
print(f"{miles} miles est égal à {meters} mètres.")
