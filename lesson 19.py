# dictionary = A changeable, unordered collection of unique key : value pairs
#              Fast because they use hashing, allow us to access a value quickly

capitals = {
    'Turkiye' : 'Ankara',
    'USA'     : 'Washington DC',
    'China'   : 'Beijing',
    'Russia'  : 'Moscow'}

capitals.update({'Germany' : 'Berlin'}) # öğe ekler
capitals.update({'USA': 'LAS VEGAS'}) # KEY değerini güncelledi
capitals.pop('China') #listeden o öğeyi siler
#capitals.clear() # tamamen siler

print(capitals['Turkiye'])
print(capitals.get('Germany')) #içine yazılı olan ifadenin sözlikte olup olmadığına bakar
print(capitals.keys()) #keys leri yazdırır
print(capitals.values()) #keys karşılıklarını yazdırır
print(capitals.items()) #keys ve karşılıklarını birlikte yazdırır

for key,value in capitals.items():
    print(key, value)
