#################################################################################
#Open file
#################################################################################

f = open(r'C:\DeepHobbying\BasicsofPython\LT18\text.txt','w')

#################################################################################
#close file
#################################################################################

f.close()
print(f.closed)

#Open file using with
with open(r'C:\DeepHobbying\BasicsofPython\LT18\text.txt','w') as f:
    pass
print(f.closed)

#################################################################################
#write file
#################################################################################

########
write
########

text="I love python"

with open(r'C:\DeepHobbying\BasicsofPython\LT18\text.txt','w') as f:
	print(f.write(text))
print(len(text))

########
write multilines
########

text="""I love python
I love R
I love Data Science\n"""
with open(r'C:\DeepHobbying\BasicsofPython\LT18\text.txt','w') as f:
	f.write(text)

########
writelines
########
text_list=['I love python\n', 'I love R\n', 'I love Data Science\n']
with open(r'C:\DeepHobbying\BasicsofPython\LT18\text.txt','w') as f:
	f.writelines(text_list)

	
	
#################################################################################
#append file
#################################################################################
text2="this is 4th line"
with open(r'C:\DeepHobbying\BasicsofPython\LT18\text.txt','a') as f:
	f.write(text2)

	
	
#################################################################################	
#read file
#################################################################################

########
read
########

with open(r'C:\DeepHobbying\BasicsofPython\LT18\text.txt','r') as f:
    print(f.read())

########
read lines efficently
########	
	
with open(r'C:\DeepHobbying\BasicsofPython\LT18\text.txt','r') as f:
    for line in f:
	    print(line)

########
readlines
########

with open(r'C:\DeepHobbying\BasicsofPython\LT18\text.txt','r') as f:
	print(f.readline())
	print(f.readline())
	print(f.readline())
	print(f.readline())

########
readlines
########

with open(r'C:\DeepHobbying\BasicsofPython\LT18\text.txt','r') as f:
	print(f.readlines())



	
#################################################################################	
#byte
#################################################################################

with open(r'C:\DeepHobbying\BasicsofPython\LT18\DeepHobbyingLogo.png','r+b') as f:
	print(f.read())


#################################################################################	
#end
#################################################################################

