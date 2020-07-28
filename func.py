def is_even(number):
    if number % 2 ==0:
        return True
    else:
        return False
print(is_even(3))
print(is_even(100))
selected=[]
def select_even(elements):
    for element in elements:
        if is_even(element)==True:
            selected.append(element)
        else:
            continue
    return selected
numbers = list(range(0, 11))
print(select_even(numbers))
print(list(filter(is_even,numbers)))
def _ends_ing(word):
    return word.endswith('ing')
c=[]
def selecting(elements):
    for element in elements:
        if _ends_ing(element):
            c.append(element)
    return c
words = ['camping', 'biking', 'sailed', 'swam']
print(selecting(words))
A=list(filter(_ends_ing,words))
print(A)
def distance(selected_individual, neighbor):
   distance_squared = (neighbor['x'] - selected_individual['x'])**2 + (neighbor['y'] - selected_individual['y'])**2
   return math.sqrt(distance_squared)

def distance_between_neighbors(selected_individual, neighbor):
    neighbor_with_distance = neighbor.copy()
    neighbor_with_distance['distance'] = distance(selected_individual, neighbor)
    return neighbor_with_distance

def distance_all(selected_individual, neighbors):
    remaining_neighbors = filter(lambda neighbor: neighbor != selected_individual, neighbors)
    return list(map(lambda neighbor: distance_between_neighbors(selected_individual, neighbor), remaining_neighbors))
    def nearest_neighbors(selected_individual, neighbors, number = None):
         number = number or len(neighbors)
        neighbor_distances = distance_all(selected_individual, neighbors)
        sorted_neighbors = sorted(neighbor_distances, key=lambda neighbor: neighbor['distance'])
    return sorted_neighbors[:number]
bob = neighbors[0]
nearest_neighbor_to_bob = nearest_neighbors(bob, neighbors, 1)
nearest_neighbor_to_bob

nearest_neighbor_to_new = nearest_neighbors({'x': 4, 'y': 3}, neighbors, 1)
nearest_neighbor_to_new

nearest_three_neighbors = nearest_neighbors({'x': 4, 'y': 3}, neighbors, 3)
nearest_three_neighbors
purchases = list(map(lambda neighbor: neighbor['purchases'],nearest_three_neighbors))
average = sum(purchases)/len(purchases)
averag


