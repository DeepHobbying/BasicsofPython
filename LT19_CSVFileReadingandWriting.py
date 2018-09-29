with open(r'C:\DeepHobbying\BasicsofPython\LT19\Test_csv.csv', 'r') as csvfile:
    print(csvfile.read())

with open(r'C:\DeepHobbying\BasicsofPython\LT19\Test_csv.csv', 'r') as csvfile:
    for line in csvfile:
        print(line)

with open(r'C:\DeepHobbying\BasicsofPython\LT19\Test_csv.csv', 'r') as csvfile:
    csvfile.__next__()
	next(csvfile)
    for line in csvfile:
        print(line.replace("\n","").split(sep=","))
####################################################################################
##Reading csv file object
import csv

with open(r'C:\DeepHobbying\BasicsofPython\LT19\Test_csv.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=",")
    csv_reader.__next__()
    csv_reader.__next__()
    print(csv_reader.line_num)

import csv

with open(r'C:\DeepHobbying\BasicsofPython\LT19\Test_csv.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=",")
    print(csv_reader)

import csv

with open(r'C:\DeepHobbying\BasicsofPython\LT19\Test_csv.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=",")
    for line in csv_reader:
        print(line)

import csv

emailid=list()
with open(r'C:\DeepHobbying\BasicsofPython\LT19\Test_csv.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=",")
    csv_reader.__next__()
    for line in csv_reader:
        emailid.append(line[2])

print(emailid)


import csv

with open(r'C:\DeepHobbying\BasicsofPython\LT19\Test_csv.csv', 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile,delimiter=",")
    for line in csv_reader:
        print(line)

####################################################################################
#writing csv
import csv

with open(r'C:\DeepHobbying\BasicsofPython\LT19\Test_csv1.csv', 'w') as csvfile:
    csv_writer = csv.writer(csvfile,delimiter="|")
    csv_writer.writerow(['Ram', 'Sharma', 'Ram_Sharma@gmail.cim', '50'])

####################################################################################
