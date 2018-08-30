import LT16_module1

from LT16_module1 import employee as ep, technical_employee as tep


emp=ep(first_name='Smruti',last_name='Ranjan',month_pay=50000)

emp.email()
print(emp.emailid)


tech_emp=tep('Vijay','Sharma',50000,"python")
tech_emp.email()
print(tech_emp.emailid)
