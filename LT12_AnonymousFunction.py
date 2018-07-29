#simple standard function

def myfun():
    print("This is a function")

myfun()	
print(myfun)


#namespace
#print(myfun)

print(sum)

def sum(a,b):
    print(a+b)

print(sum)


#lambda expression

x=lambda:print("This is a function")

print(x)

#simple example
y=lambda x:x**2+2

print(y(2)

#complex example


my_list=[23,45,4,89,46,23,346,58,24,27]
print(my_list)

#Filter out all the odd items with in the list : my_list
#lambda with filter

lambda x: x%2 != 0

my_list2=list(filter(lambda x: x%2 != 0,my_list))
print(my_list2)

#Increase each item of list : my_list by 2
#lambda with map

my_list3=[item+2 for item in my_list]
my_list3=list(map(lambda x:x+2,my_list))

print(my_list3)


