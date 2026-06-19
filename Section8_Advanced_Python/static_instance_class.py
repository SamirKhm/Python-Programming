class Employee:
    company="HP"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # instance method - default method, takes self as the first parameter, can be called on the instance
    def print_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Company: {Employee.company}")

    # static method - dont requires self parameter, can be called on the class itself
    @staticmethod
    def sum(a,b):
        return a+b
    
    # class method - takes cls as the first parameter, can be called on the class itself
    @classmethod
    def print_company(cls):
        print(f"Company: {cls.company}")

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company
        print(f"Company changed to: {cls.company}")


e1=Employee("John Doe", 50000)
e2=Employee("Sam Curran", 60000)
e1.print_info()
e2.print_info()
print(e1.company)  # Output: HP
print(e2.sum(3,4))  # Output: 7 # passes self by default

print(Employee.sum(3,4))  # Output: 7 # does not pass self by default

Employee.print_company()  # Output: Company: HP
e1.print_company()  # Output: Company: HP
e1.change_company("Microsoft")  # Output: Company changed to: Microsoft
Employee.print_company()  # Output: Company: Microsoft