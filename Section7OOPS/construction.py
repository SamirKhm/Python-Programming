class Employee:
    def __init__(self,salary,name,bond):
        self.salary=salary # instance variable salary is initialized with the value passed as an argument when creating an object of the class Employee
        self.name=name
        self.bond=bond

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        return f"Name: {self.name}, Salary: {self.salary}, Bond: {self.bond} years"

e1=Employee(45000,"John",2) # creating an object of the class Employee
print(e1.get_salary()) # calling the method get_salary() of the object e1

e2=Employee(50000,"Jane",3) # creating another object of the class Employee
print(e2.get_salary()) # calling the method get_salary() of the object e2

print(e1.get_info()) # calling the method get_info() of the object e1
print(e2.get_info()) # calling the method get_info() of the object e2