if __name__ == "__main__":
    print("this is moddule1 and run from module1")
else:
    print("this is module1 but run from module2")


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
        self.prog_lang=prog_lang
