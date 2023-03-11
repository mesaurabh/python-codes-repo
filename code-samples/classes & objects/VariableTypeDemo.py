class Employee:
    # class variable
    companyName = "ABC Company"

    def __init__(self, fname, lname):
        # instance variable
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f"Employee details are : {self.fname} {self.lname} {self.companyName}"


emp1 = Employee("ana", "williams")
print(emp1)
