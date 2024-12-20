class Student:

    def __init__(self,name,standard,section,address):
        self.name = name
        self.standard = standard
        self.section = section
        self.address = address

    def __str__(self):
        return "Name : "+self.name+" - Standard : "+self.standard+" - Section : "+self.section+" - Address : "+self.address
