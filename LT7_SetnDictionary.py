##Set
myset1={23,85,64,72,5,10,87,23}
print(myset1)

#membership operation
print(23 in myset1)


myset2={23,56,87,10}
print(myset1.intersection(myset2))
print(myset1.difference(myset2))
print(myset1.union(myset2))

#Dictionary
x={'red':1,'green':2,'black':3,'pink':4,'yellow':5}
print(x.keys())
print(x.values())

print(x.get('red','not found'))

x.update({'red':12,'green':13,'white':25})
print(x)

del x['red']
print(x)

print(x.pop('green'))
print(x)



    

















