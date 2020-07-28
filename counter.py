t="the quick brown fox jumped over the lazy cow"
text=t.lower()
counter={}
for char in text:
    if char not in counter:
        counter[char] = 1
    else:
        counter[char]+=1
print(counter)
li = ['a','b','c']
print(li)
li.reverse()
print(li)
a = ['a','b','c']
b = [1,2,3]
print([(k,v) for k,v in zip(a,b)])
lit = ['a','b','c','d','e']
for i,val in enumerate(lit):
    print(str(i+1)+"."+ str(val))
a = [1,2,3,4,5]
 
a2 = [x+1 for x in a]
print(a2)
print('123'.isnumeric())
print("abcd".isalpha())
print('123abc'.isalnum())
d = {'id':7, 'name':'Shiba', 'color':'brown', 'speed':'very slow'}
print(list(d))
city_indices = list(range(12))
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
names_and_ranks = [] 
for index in city_indices: 
    names_and_ranks.append(f"{index + 1}. {city_names[index]}")
print(names_and_ranks)
def times_two(a):
    b=[]
    for i in range(len(a)):
        b.append(a[i]*2)
    return b
A=[1,2,3]
B=times_two(A)
C=list(map(lambda x: x*2,A))
if B==C:
    print("Same!")
else:
    print("Wrong!")
D={k+1:v for (k,v) in enumerate(city_names)}
print(D)
a = ['c','b','a']
b = [1,2,3]
c=[(k,v) for k,v in zip(a,b)]
print(sorted(c))
e = {'c':3, 'd':4, 'b':2, 'a':1}
print(sorted(e.items()))
