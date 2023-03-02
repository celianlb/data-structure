def rechercher_emplois(emplois, recherche):
    emplois_trouves = []
    for emploi in emplois:
        if any(filter(lambda v: isinstance(v, str) and recherche.lower() in v.lower(), emploi.values())):
            emplois_trouves.append(emploi)
    return emplois_trouves
