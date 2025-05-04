class Employee:
    company = "Sprinklr"

    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary

    # Instance Method (Default method)
    def print_info(self):
        info = f"The name is {self.name} and salary is {self.salary}"
        print(info)

    def sum(self,a,b):
        return a+b 
    
    @staticmethod
    def sum2(a,b):
        return a+b 
    
    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company

e1 = Employee("Tejas",50000)
e2 = Employee("Ravi",10000)
print(Employee.company)
# print(Employee.name) Attribute Error

e1.print_info()
e2.print_info()
print(e1.sum(2,3))
print(e1.sum2(2,3))

e1.print_company()
print(Employee.company)
e1.change_company("Amex")
e1.print_company()
print(Employee.company)