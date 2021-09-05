#parent class - > property and method(super class or base class)
#child class -> child class extends parent class

#Company parent class
#Employee ->child class

#parent class
class Company:
    def __init__(self,cname,caddress):
        self.company_name = cname
        self.company_address = caddress
    
    def getCompanyName(self):
        return self.company_name

#child class
class Employee(Company):
    def __init__(self,cname,caddress,empid,empname):
        #using super keyword
        # super().__init__(cname,caddress)
        
        #using class name
        Company.__init__(self,cname,caddress)
        self.emp_id = empid
        self.emp_name = empname
    
    def getEmployeeName(self):
        self.emp_name


e = Employee("MNC Company","Delhi",1,"Rahul")
# print(e.emp_id,e.emp_name)
# print(e.company_name,e.company_address)

print("My name is",e.emp_name,"and company name is",e.company_name)