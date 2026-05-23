class Car:
    def __init__(self,name):
        self.name=name

    def drive(self):
        print(f"{self.name} is driving")

d=Car("Toyota")
d.drive() # Output: Toyota is driving

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print(f"Name: {self.name}, Age: {self.age}")

p=Person("Alice",30)
p.info() # Output: Name: Alice, Age: 30
        

