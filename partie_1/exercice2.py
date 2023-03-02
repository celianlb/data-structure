
"""
exercice 2
"""
nom2=["Malek le tricher","Nagaakira","Mitsuakira","Tsunaakira","Tsunanaga"]
def ajout(nom2, ajout):
    nom2.append(ajout)
    print(nom2)

def supp(nom2, supp):
    if supp in nom2:
        nom2.remove(supp)
        print(nom2)

    else:
        print("Element non trouver") 

ajout(nom2, "Axel")
supp(nom2, "Axel")
supp(nom2, "Axel")
