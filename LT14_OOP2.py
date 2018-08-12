###########################################
#####class method1

class employee:
    def __init__(self,first_name,last_name,month_pay):
        self.first_name=first_name
        self.last_name=last_name
        self.month_pay=month_pay

    def email(self):
        return self.first_name+'_'+self.last_name+'@gmail.com'
    def __del__(self):
        pass

emp1=employee(first_name='Smruti',last_name='Ranjan',month_pay=30000)
emp2=employee('Vijay','Sharma',50000)

print(emp1.email())
print(employee.email(emp1))



###########################################
#####class method2

class employee:
    def __init__(self,first_name,last_name,month_pay):
        self.first_name=first_name
        self.last_name=last_name
        self.month_pay=month_pay

    def email(self):
        self.emailid = self.first_name+'_'+self.last_name+'@gmail.com'
    def __del__(self):
        pass

emp1=employee(first_name='Smruti',last_name='Ranjan',month_pay=30000)
emp2=employee('Vijay','Sharma',50000)

print(emp1.email())
print(emp1.emailid)

emp2.email()
print(emp2.emailid)

###########################################
#####class variables

class employee:
    comp_factor = 1.5
    emp_factor = 1
    def __init__(self,first_name,last_name,month_pay):
        self.first_name=first_name
        self.last_name=last_name
        self.month_pay=month_pay

    def email(self):
        self.emailid = self.first_name+'_'+self.last_name+'@gmail.com'


    def raise_amount(self):
        self.month_pay *= (self.comp_factor*self.emp_factor)
        
    def __del__(self):
        pass

emp1=employee(first_name='Smruti',last_name='Ranjan',month_pay=30000)
emp2=employee('Vijay','Sharma',50000)

print(emp1.month_pay)
emp1.raise_amount()
print(emp1.month_pay)


print(emp2.month_pay)
emp2.emp_factor=2
emp2.raise_amount()
print(emp2.month_pay)


###########################################
#####class method

class employee:
    comp_factor = 1.5
    emp_factor = 1
    def __init__(self,first_name,last_name,month_pay):
        self.first_name=first_name
        self.last_name=last_name
        self.month_pay=month_pay

    def email(self):
        self.emailid = self.first_name+'_'+self.last_name+'@gmail.com'


    def raise_amount(self):
        self.month_pay *= (self.comp_factor*self.emp_factor)
        
    def __del__(self):
        pass

    @classmethod
    def comp_amount(cls,amount):
        cls.comp_factor=amount

emp1=employee(first_name='Smruti',last_name='Ranjan',month_pay=30000)
emp2=employee('Vijay','Sharma',50000)

print(employee.comp_factor)
print(emp1.comp_factor)
print(emp2.comp_factor)

employee.comp_amount(1.6)

print(employee.comp_factor)
print(emp1.comp_factor)
print(emp2.comp_factor)
