x=[1,2,10,18,3,4]

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
print('Once i became 2, the value of x[2] became 10. Hence, the if statement executed and brock the loop.')

#continue

i=0

while i<=len(x)-1:
    if i==3:
        i=4
        continue
    print(x[i])
    i+=1
print('Once i became 3, if statement executed and assign new value of i as 4 and then continued. Hence, it ignored printing x[4] (which is 18) and move to the next iteration of loop.')


#pass

i=0

while i<=len(x)-1:
    if x[i]==10:
        pass
    print(x[i])
    i+=1
print('Once i became 2, the value of x[2] became 10. Hence, the if statement executed which is doing nothing rather than just pass the if statement.')

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
