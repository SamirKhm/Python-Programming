# decorators

def logger(func):
    def wrapper():
        print("Function is called")
        func()
    return wrapper

@logger
def say_hello():
    print("Hello, World!")

say_hello()

def timer(func):
    def wrapper():
        import time
        t1=time.time()
        func()
        t2=time.time()
        print(f"Time taken: {t2-t1} seconds")
    return wrapper

@timer
def sum():
    total = 0
    for i in range(1, 1000001):
        total += i
    return total

print(sum())

# getters and setters

class Employee:
    _salary=34

    def __init__(self, salary):
        self._salary = salary  

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value

emp = Employee(50000)
print(emp.salary) # this will call the getter method

emp.salary = 60000 # this will call the setter method
print(emp.salary)
# emp.salary = -1000 # this will raise a ValueError because the setter method checks for negative values


# static methods and class methods

class Math:
    @staticmethod
    def add(a,b):
        return a+b

    @classmethod
    def description(cls):
        return "This is a Math class"
    
a=Math.add(5,10) # this will call the static method
print(a)
print(Math.description()) # this will call the class method


# magic methods 


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        return len(self.title)
book = Book("The Great Gatsby", "F. Scott Fitzgerald")

print(str(book)) # this will call the __str__ method
print(len(book)) # this will call the __len__ method

