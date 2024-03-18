dictionary_of_Alex = {'favourite colour': 'blue', 'favourite food': 'pasta', 'favourite animal': 'fish','favourite hobby': 'swimming'}
print (dictionary_of_Alex.keys())
print (dictionary_of_Alex.values())
print (dictionary_of_Alex.items())
print ('favourite colour' in dictionary_of_Alex)
print ('favourite movie' not in dictionary_of_Alex)
print (dictionary_of_Alex.get('favourite colour'))
dictionary_of_Alex ['favourite colour'] = 'aqua'
dictionary_of_Alex ['favourite food'] = 'marinara pasta'
dictionary_of_Alex ['favourite animal'] = 'whale shark'
dictionary_of_Alex ['favourite hobby'] = 'ocean swimming'
print (dictionary_of_Alex)
dictionary_of_Alex ['favourite movie'] = 'Castaway'
print (dictionary_of_Alex)
dictionary_of_Alex.pop( 'favourite food')
print (dictionary_of_Alex)
favourites = dictionary_of_Alex.copy()
print (favourites)
for key, value in favourites.items():
  print (key, value)
user = ['Alex']
user_info = {'first name': 'Alex', 'favourites list': favourites}
print (user_info)