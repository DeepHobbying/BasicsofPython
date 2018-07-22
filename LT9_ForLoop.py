#General For Loop


x = ["black","green","red","yellow","white","pink"]

for i in x:
    print(i)

 
for i in enumerate(x):
    print(i[1])



#One Liner Advantage

y = [51,2,74,57,89,346]


z = list()  #[]

print(z)

for k in y:
    z.append(k+2)

print(z)


print([k+2 for k in y])     #One Liner
