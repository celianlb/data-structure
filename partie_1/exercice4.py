


"""
exercice 4
"""

dictionary = {
    "Nagaakira": 25,
    "Mitsuakira": 33,
    "Tsunaakira": 39
}

def present(dictionary, cle):

    return cle in dictionary

def ajouter(dictionary, cle, valeur):
    dictionary[cle] = valeur

print(present(dictionary, "Tsunaakira"))

ajouter(dictionary, "Tsunaakira",40)
print(dictionary)
