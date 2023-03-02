list = [{'nom': 'Clan Asano', 'membres': 50, 'chef': 'Yoshiteru'},
        {'nom': 'Clan Hiroshima', 'membres': 40, 'chef': 'Narikata'},
        {'nom': 'Clan Munetsune', 'membres': 35, 'chef': 'Shigeakira'}]

print(len(list))

print(max(list, key=lambda clan: clan['membres'])['nom'])


