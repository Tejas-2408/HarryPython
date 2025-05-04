class Employee:

    def __init__(self,salary,name,bond=0):  ## Constructor to define basic properties
        self.salary = salary
        self.name = name
        self.bond = bond

    def get_salary(self):
        return self.salary
    

e1 = Employee(50000,"Tejas",2)
e2 = Employee(100000,"Ravi",3)

print(e1.get_salary())
print(e2.get_salary())