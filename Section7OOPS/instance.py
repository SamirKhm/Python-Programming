class Employee:
    company="HP"

    def __init__(self,salary,name,bond,company):
        self.salary=salary # instance variable salary is initialized with the value passed as an argument when creating an object of the class Employee
        self.name=name
        self.bond=bond
        self.company=company

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        return f"Name: {self.name}, Salary: {self.salary}, Bond: {self.bond} years and Company: {self.company}"

e1=Employee(45000,"John",2,"ASUS") # creating an object of the class Employee
print(e1.company) # accessing the class attribute company using the object e1
print(Employee.company) # accessing the class attribute company using the class Employee

# Object introspection is the ability to examine the type or properties of an object at runtime. It allows us to check the attributes and methods of an object, and to determine the type of an object.

print(dir(e1)) # using the built-in function dir() to get a list of all the attributes and methods of the object e1