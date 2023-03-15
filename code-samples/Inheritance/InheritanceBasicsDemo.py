class Person:
    def __init__(self, firstname, lastname, city, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.city = city
        self.gender = gender

    def printPersonDetails(self):
        print("Person details : ", self.firstname, self.lastname, self.city, self.gender)


class Employee(Person):
    def __init__(self, firstname, lastname, city, gender, company, salary):
        # Actual class name can be replaced with the super() function, because super() will internally call Person
        # class in this example

        # Person.__init__(self, firstname, lastname, city, gender)
        super().__init__(firstname, lastname, city, gender)
        self.company = company
        self.salary = salary

    def printEmpDetails(self):
        print("Employee details are : ", self.firstname, self.lastname, self.city, self.gender, self.company,
              self.salary)


emp1 = Employee("Sohail", "Shaik", "USA", "Male", "IBM", 90000)
emp1.printEmpDetails()
