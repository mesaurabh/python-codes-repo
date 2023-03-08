class Person:
    # first_name, last_name, city
    # init() method --> it acts like a constructor
    def __init__(self, firstName, lastName, city):
        self.firstName = firstName
        self.lastName = lastName
        self.city = city

    def __str__(self):
        return f"{self.firstName} {self.lastName} {self.city}"


person1 = Person("Saurabh", "Deshpande", "Pune")
print(person1)

person2 = Person("Sohail", "Shaik", "USA")
print(person2)