list = [{'nom': 'Malek le tricheur', 'score': 1000, 'niveau': 5},
        {'nom': 'Nagaakira', 'score': 800, 'niveau': 4},
        {'nom': 'Mitsuakira', 'score': 700, 'niveau': 3},
        {'nom': 'Tsunaakira', 'score': 600, 'niveau': 2},
        {'nom': 'Tsunaaga', 'score': 500, 'niveau': 1},]

print(sorted(list, key=lambda joueur: joueur['score'], reverse=True))

print(sorted(list, key=lambda joueur: joueur['score'], reverse=True)[:3])

def level_function(score):
    if score >= 1000:
        return 5
    elif score >= 800:
        return 4
    elif score >= 700:
        return 3
    elif score >= 600:
        return 2
    else:
        return 1
print(level_function(1000))        


def avg_score(list):
    return sum(joueur['score'] for joueur in list) / len(list)
print(avg_score(list))


def update_score(list, name, score):
    for joueur in list:
        if joueur['nom'] == name:
            joueur['score'] = score
            break
    return list
print(update_score(list, 'Tsunaaga', 1000))

#Crée une fonction qui accepte 3 input utilisateur : nom, score, niveau. Vérifiez que le nom n'existe pas déjà dans la liste s'il n'existe pas ajouter le joueur a la liste et afficher les 3 joueurs avec le plus gros score
def add_player(list, name, score, level):
    for joueur in list:
        if joueur['nom'] == name:
            return "Le nom existe déjà"
    list.append({'nom': name, 'score': score, 'niveau': level})
    return sorted(list, key=lambda joueur: joueur['score'], reverse=True)[:3]
print(add_player(list, 'Tsunaaga', 1000, 5))