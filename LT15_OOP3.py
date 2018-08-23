
#################################################
#statics method

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

    @staticmethod
    def leap_year(year):
        if year%4==0:
            return "it is a leap year"
        else:
            return "it is not a leap year"

emp1=employee(first_name='Smruti',last_name='Ranjan',month_pay=30000)
emp2=employee('Vijay','Sharma',50000)

print(employee.leap_year(2016))
print(emp1.leap_year(2000))


#################################################
#Inhertance

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

    @staticmethod
    def leap_year(year):
        if year%4==0:
            return "it is a leap year"
        else:
            return "it is not a leap year"

class technical_employee(employee):
    def __init__(self,first_name,last_name,month_pay,prog_lang):
        super().__init__(first_name,last_name,month_pay)
        #employee.__init__(self,first_name,last_name,month_pay)
        self.prog_lang=prog_lang
        
        

emp=employee(first_name='Smruti',last_name='Ranjan',month_pay=50000)
tech_emp=technical_employee('Vijay','Sharma',50000,"python")


tech_emp.email()
print(tech_emp.emailid)

print(help(technical_employee))
print(isinstance(tech_emp,technical_employee))
print(issubclass(technical_employee,employee))

print(emp.month_pay)
print(tech_emp.month_pay)

emp.raise_amount()
tech_emp.raise_amount()

print(emp.month_pay)
print(tech_emp.month_pay)


print(tech_emp.prog_lang)



