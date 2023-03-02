"""
exo3
"""
def binaire(n):
    
    

    if isinstance(n, int) or n>0:
        if n == 0:
            return "0"
        bit = ""
        while n > 0:
            bit = str(n % 2) + bit
            n //= 2
        return bit
    else:
        return "Erreur : l'entrée doit être un nombre entier positif."
print(binaire(434))
