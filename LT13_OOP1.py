class employee:
    pass

emp1 = employee()

emp2 = employee()


print(emp1)
print(emp2)


emp1.first_name='Smruti'
emp1.last_name='Ranjan'
emp1.month_pay=30000

emp2.first_name='Vijay'
emp2.last_name='Sharma'
emp2.month_pay=50000

print(emp1.first_name)

###########################################

class employee:
    def __init__(self,first_name,last_name,month_pay):
        self.first_name=first_name
        self.last_name=last_name
        self.month_pay=month_pay

emp1 = employee(first_name='Smruti',last_name='Ranjan',month_pay=30000)

emp2 = employee('Vijay','Sharma',50000)

print(emp1.first_name)


###########################################

class employee:
    def __init__(self,first_name,last_name,month_pay):
        self.first_name=first_name
        self.last_name=last_name
        self.month_pay=month_pay

    def __del__(self):
        pass

emp1=employee(first_name='Smruti',last_name='Ranjan',month_pay=30000)
emp2=employee('Vijay','Sharma',50000)


print(emp1.first_name)
