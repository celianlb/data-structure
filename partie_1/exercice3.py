"""
exercice 3
"""
a="Malek le tricheur n'est pas un vrai samourai"

b=a.split()
print(str(len(b)))
fusion = " ".join(b)
print(fusion)


if 'tricheur' in b:
    print("'tricheur' est trouvé dans la liste : " , b)
else:
    print("'tricheur' n'est pas trouvé dans la liste : " , b)
