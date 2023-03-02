#Exercice 5 : itérations de lettres. Créez une fonction qui prend en entrée un mot et retourne le nombre de fois où chaque lettre apparaît dans ce mot.  Les lettres doivent être retournées en ordre croissant d’occurrence, puis en tri alphabétique pour les valeurs ayant le même nombre d’occurrences.


def letter_occurrences(word):
    return {letter: word.count(letter) for letter in sorted(word)}

print(letter_occurrences("chevre"))



