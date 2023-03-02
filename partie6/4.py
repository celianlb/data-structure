class Ville:
    def __init__(self, nom):
        self.nom = nom
        self.routes = {}
        
    def ajouter_route(self, ville, distance, vitesse):
        temps = distance / vitesse
        self.routes[ville] = {'distance': distance, 'temps': temps}
        
class Carte:
    def __init__(self):
        self.villes = {}
        
    def ajouter_ville(self, nom):
        ville = Ville(nom)
        self.villes[nom] = ville
        
    def ajouter_route(self, ville1, ville2, distance, vitesse):
        self.villes[ville1].ajouter_route(ville2, distance, vitesse)
        self.villes[ville2].ajouter_route(ville1, distance, vitesse)


def temps_min(carte, ville1, ville2):
    distances = {ville1: 0}
    temps = {ville1: 0}
    visites = {ville1}
    en_cours = ville1
    
    while en_cours != ville2:
        if en_cours is None:
            raise ValueError('Il n\'existe pas de chemin entre ces deux villes')
        
        for ville, route in carte.villes[en_cours].routes.items():
            nouvelle_distance = distances[en_cours] + route['distance']
            nouveau_temps = temps[en_cours] + route['temps']
            
            if ville not in visites or distances[ville] > nouvelle_distance:
                visites.add(ville)
                distances[ville] = nouvelle_distance
                temps[ville] = nouveau_temps
                
        en_cours = None
        for ville in visites:
            if ville not in distances:
                continue
            if en_cours is None or distances[ville] < distances[en_cours]:
                en_cours = ville
                
    return temps[ville2]