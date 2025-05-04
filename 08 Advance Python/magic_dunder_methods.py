class Employee:
    company = "Sprinklr"
    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary

    def __str__(self):
        return f"The name is {self.name} with salary {self.salary}"
    
    def __len__(self):
        return len(self.name)
    
e1 = Employee("Tejas",50000)
# print(e1.name,e1.salary)

# print(str(e1))
print(len(e1))