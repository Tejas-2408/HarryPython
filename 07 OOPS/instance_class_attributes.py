class Employee:
    company = "Dell"  # this is class attribute

    def __init__(self,salary,name,bond,company):  ## Constructor to define basic properties
        self.salary = salary
        self.name = name
        self.bond = bond
        self.company = company

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of Employee is {self.name} with salary {self.salary}. The bond of Employee is {self.bond} years")

    
e1 = Employee(50000,"Tejas",2,"Sprinklr")
print(e1.company) # will always print instance attribute whenever present
print(Employee.company)

## Object Introspection
print(dir(e1))