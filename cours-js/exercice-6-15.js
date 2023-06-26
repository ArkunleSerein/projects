// exo 6.15
// Trouvez la chaîne de caractères la plus longue dans une liste.
// Affichez son index, sa valeur et sa longueur.
//
// ATTENTION : ne pas utiliser la fonction list.index()
// ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

let my_list = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']

// réponse 6.15

// my_list.length
for (let i = 0; i < my_list.length; i++) {
    console.log(i);
    console.log(my_list[i]);
    console.log(my_list[i].length);
}