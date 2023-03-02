


"""
    exo 7
"""
import random
import string
def setfusion(set1,set2):
    print(set1)
    print(set2)
    set=set1.union(set2)
    print(set)
    set1_decroissant = sorted(set1, reverse=True)
    set2_decroissant = sorted(set2, reverse=True)
    
    print(set1_decroissant)
    print(set2_decroissant)

    somme_set1=sum(set1)
    print(somme_set1)
    somme_set2=sum(set2)
    print(somme_set2)
    somme_set=sum(set)
    print(somme_set)

    chaine=''.join(random.choice(string.ascii_lowercase) for i in range(somme_set))
    print(chaine)
    dictionary_set={'union set': set, 'set1 decroissant': set1_decroissant, 'set2 decroissant': set2_decroissant, 'somme des 2 sets': somme_set, 'lorem': chaine}
    return dictionary_set
set1={1,2,3,4}
set2={5,6,7,8}

reseult=setfusion(set1,set2)

print(reseult)
