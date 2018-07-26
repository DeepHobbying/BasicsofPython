x=[1,2,10,2,3,4,5]

#while

i=0

while i<=len(x)-1:
    print(x[i])
    i+=1

#break

i=0

while i<=len(x)-1:
    if x[i]==10:
        break
    print(x[i])
    i+=1
print('break')

#continue

i=0

while i<=len(x)-1:
    if i==3:
        i=7
        continue
    print(x[i])
    i+=1
print('continue')


###pass

i=0

while i<=len(x)-1:
    if x[i]==10:
        pass
    print(x[i])
    i+=1
print('pass')

#Try & Except

i=0


while True:
    try:
        print(x[i])
    except:
        break
    i+=1
        

##while True:
##    print(x[i])
##    i+=1
