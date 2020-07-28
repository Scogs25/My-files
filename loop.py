names_and_ranks = [] 
city_indices=list(range(12))
city_names = ['Buenos Aires',
 'Toronto',
 'Marakesh',
 'Albuquerque',
 'Los Cabos',
 'Greenville',
 'Archipelago Sea',
 'Pyeongchang',
 'Walla Walla Valley',
 'Salina Island',
 'Solta',
 'Iguazu Falls']
for index in city_indices: 
    names_and_ranks.append(f"{index + 1}. {city_names[index]}")
print(names_and_ranks[0])
print(names_and_ranks[1])
print(names_and_ranks[-1])
city_populations = []
for city in cities:
    city_populations.append(city['Population'])
city_populations
city_areas = []
for city in cities:
    city_areas.append(city['Area'])