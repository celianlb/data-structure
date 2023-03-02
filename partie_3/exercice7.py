def hiearchie_fichier(fichier, chemin):
    
    
    for cle in fichier:
        chemin+=f"{cle['name']}/"
        
        if cle['type']=='file':
            str = ' '.join(chemin) 
            print(str.replace(" ", ""))  
        elif cle['type']=='directory':
            chemin+=f"{cle['name']}/"
            hiearchie_fichier(cle['children'], chemin)
            

            
fichier=  [
    {
        'name': 'python',
        'type': 'directory',
        'children': [
            {
                'name': 'exercice7.py',
                'type': 'file'
            },
            {
                'name': 'partie3',
                'type': 'directory',
                'children': [
                    {
                        'name': 'exercice7.py',
                        'type': 'file'
                    }
                ]
            }
        ]
    }
]
chemin=[]
hiearchie_fichier(fichier, chemin)