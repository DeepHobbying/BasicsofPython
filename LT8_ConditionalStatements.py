#ConditionalStatements

#if

x = int(input("please put a number:"))

if x%2 == 0:
    print("this is an even number")


#if else

x = int(input("please put a number:"))

if x%2 == 0:
    print("this is an even number")
else:
    print("this is an odd number")


#if elif else 

x = int(input("please put a number:"))

if x%2 == 0:
    print("this is an even number")
elif x%7 == 0:
    print("this number is divisible by 7")
else:
    print("this is an odd number")


# nested if

x = int(input("please put a number:"))

if x%2 == 0:
    if x%5 == 0:
       print("this is an even number also divisible by 5")
    else:
        print("this is an even number but not divisible by 5")
else:
    print("this is an odd number")

