# dunder - __ methods, double underscore methods

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employee(name={self.name}, salary={self.salary})"

    def __repr__(self):
        return f"Employee(name={self.name}\nsalary={self.salary})"

    def __len__(self):
        return len(self.name)


e=Employee("John Doe", 50000)
print(e.name)
print(len(e))
print(str(e))  # Output: Employee(name=John Doe, salary=50000)

print(repr(e))  # Output: Employee(name=John Doe, salary=50000)


 