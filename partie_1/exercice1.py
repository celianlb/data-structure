"""
exercice 1
"""
nom=["Malek le tricher","Nagaakira","Mitsuakira","Tsunaakira","Tsunanaga"]
def list(nom,i):   
    if len(nom)>i:
        return nom[i]
    else:
        return "i trop grand"
i=2
print(list(nom,i))
