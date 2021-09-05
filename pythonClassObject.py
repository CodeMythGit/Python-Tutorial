class Student:

    def __init__(self):
        print(" inside init method ")
        self.name = "John"
        self.age = 40
        self.years = "2021"
    
    def printDetails(self,name,years):
        print(self.name,self.years)
        # print(name,years)

s = Student()
print(s.name,s.age)

#init methpd

s.printDetails("Rocky","2001")

s.age = 25
print(s.name,s.age)

#delete property
del s.age
# print(s.age)

#delete object
del s
print(s)

class Person:
    pass
