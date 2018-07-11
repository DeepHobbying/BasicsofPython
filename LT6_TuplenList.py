#tuple
my_tup=("Red", "Green", "Blue", "White", "Pink", "Black")
#print(type(my_tup))
#print(len(my_tup))

#slicing using index (Note: this is same for list as well)

print(my_tup[0]) # will return Red
print(my_tup[1:4])  #will return ('Red', 'Green', 'Blue')
print(my_tup[1:]) #will return ('Red', 'White', 'Green', 'Blue', 'White', 'Pink', 'Black')
#print(my_tup[10]) # python will return error, because maximum index assigned to this tuple is 5
print(my_tup[1:10]) # Python will return the entire tuple starting from index 1

#operation that you can perform on tuple (Note: this is same for list as well)

print(my_tup.count('Red')) # you will get the output 1 as red is appearing once in the tuple
print(my_tup.index('Red')) # 0 will be the output as the index of element "Red" in tuple is 0


#List (Run the below code individually and see if you can get the same result as in tutorial)

my_list=["Red", "Green", "Blue", "White", "Pink", "Black"]
#print(type(my_list))
#print(len(my_list))
my_list2=[1,2]

my_list=["Red", "Green", "Blue", "White", "Pink", "Black"]
my_list.append("Yellow")
print(my_list)

my_list=["Red", "Green", "Blue", "White", "Pink", "Black"]
my_list.insert(2,"Yellow")
print(my_list)

my_list=["Red", "Green", "Blue", "White", "Pink", "Black"]
my_list.extend(my_list2)
print(my_list)

my_list=["Red", "Green", "Blue", "White", "Pink", "Black"]
my_list.remove("White")
print(my_list)

my_list=["Red", "Green", "Blue", "White", "Pink", "Black"]
print(my_list.pop())
print(my_list)

my_list.sort()
my_list.reverse()
print(my_list)











