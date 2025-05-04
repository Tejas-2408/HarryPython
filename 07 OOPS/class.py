# Class: Class is a blueprint or a template. E.g., Form for an Exam that contains name,age,electives, father's name


# Objects: Specific instance created from the template (class). Form containing information of canditate 

class Employee:
    company = "Sprinklr"

    def get_salary(self):  # Mandatory to pass first parameter as Self as it refer to the object which calls the function
        print(self)
        return 50000
    

e1 = Employee()
print(e1.get_salary())

e2 = Employee()
print(e2.get_salary())
print(e2.company)