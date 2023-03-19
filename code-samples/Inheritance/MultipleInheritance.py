class Person:
    def personInfo(self, name, age):
        print('Name : ', name, 'Age : ', age)


class Company:
    def companyInfo(self, companyName, location):
        print('Company Name  : ', companyName, 'Location : ', location)


class Employee(Person, Company):
    def empInfo(self, salary, department):
        print('Employee salary : ', salary, 'Employee department : ', department)


emp1 = Employee()
emp1.personInfo('Saurabh', 35)
emp1.companyInfo('IBM', 'Pune')
emp1.empInfo(90000, 'Cloud Engineering')
