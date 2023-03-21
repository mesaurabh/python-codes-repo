class Organisation:

    def __init__(self):
        # Protected variable
        self._assignment = "Python Training"


class Employee(Organisation):

    def __init__(self, name, salary):
        # public variable
        self.name = name

        # private variable
        self.__salary = salary
        super().__init__()

    def displayDetails(self):
        print("Name = ", self.name, "Salary = ", self.__salary)
        print("Printing assignment name from Organisation class : ", self._assignment)


emp = Employee("Saurabh", 90000)
emp.display()
