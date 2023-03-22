class Customer:
    def __init__(self, fname, lname, ssn):
        self.fname = fname
        self.lname = lname
        self.__ssn = ssn

    # Getter method for ssn
    def get_ssn(self):
        return self.__ssn

    # Setter method for ssn
    def set_ssn(self, ssn):
        self.__ssn = ssn

    def get_firstname(self):
        return self.fname

    def set_firstname(self, fname):
        self.fname = fname


customer1 = Customer("Saurabh", "Deshpande", "rrr-444-666")
print("Current ssn for customer1 is :  ", customer1.get_ssn())
print("Current firstname for customer1 is :  ", customer1.get_firstname())

customer1.set_ssn("srd-777-888-rrr")
customer1.set_firstname("Sourabh")

print("Current ssn for customer1 is :  ", customer1.get_ssn())
print("Current firstname for customer1 is :  ", customer1.get_firstname())
