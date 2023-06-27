// en JS let permet d'inscire une variable dans un scope local
// tandis que var permet d'inscrire une variable dans une scope semi-local

for (let i = 0; i < 10; i++) {
    console.log(i);
}
// si la variable i a était définie avec le mot clé let.
// i n'est accessible que si elle a été définie dans la même scope ou un scope extérieur
console.log(i);

for (var i = 0; i < 10; i++) {
    console.log(i);
}

// si la variable i a été définie avec le mot clé var, elle est accessible même si elle a été définie dans un scope intérieur
console.log(i);

function myFunc1() {
    var myVar1 = 123;
}

// même si la variable myVar1 est déclarée avec le mot clé var, comme elle est déclarée à l'intérieur d'une fonction, elle n'est pas accessible depuis un scope extérieur
// ReferenceError: myVar1 is not defined
//console.log(myVar1);

 //_____________________________________//  LES CLOSURE //___________________________________//

 function multNFactory(n) {
    return function multN(x) {
        return x * n;
    }
 }

 mult3 = multNFactory(3);

 for (let i = 0; i < 3; i++) {
        console.log(mult3(i));
 }

 mult54 = multNFactory(54);

 for (let i = 0; i < 3; i++) {
    console.log(mult54(i));
}

 //_____________________________________//  LES CLOSURE //___________________________________//