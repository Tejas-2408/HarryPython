class Employee:
    def __init__(self,name,salary):
        self.salary = salary
        self.name = name 
    @property
    def first_name(self):
        l = self.name.split(" ")
        return l[0]
    
    @first_name.setter
    def first_name(self,first):
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}"
        self.name = new_name
    

e = Employee("Tejas bansal",50000)
# print(e.first_name())
# e.set_first_name("Ravi")
# print(e.first_name())

print(e.first_name)
e.first_name = "Ram"
print(e.first_name)