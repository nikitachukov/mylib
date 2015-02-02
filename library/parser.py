my_dict = {'name': 'Lancelot', 'quest': 'Holy Grail', 'favourite_color': 'blue'}

print(my_dict.get('airspeed velocity of an unladen swallow', 'African or European?\n'))

for key,value in my_dict.items():
    print( key,value, sep=": ")