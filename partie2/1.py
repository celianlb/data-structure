def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Les deux chaînes doivent avoir la même longueur.")
    return sum(c1 != c2 for c1, c2 in zip(str1, str2))
    
print(hamming_distance("chevre", "chovre"))
print(hamming_distance("oui", "non"))