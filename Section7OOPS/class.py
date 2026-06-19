
# class is a blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class will have.
# object is an instance of a class. It is created from the class and has the attributes and methods defined in the class.

class Employee:
    company="HP"

    def get_salary(self):
        print(self)
        return 45000

# self- is a reference to the current instance of the class. It is used to access the attributes and methods of the class in Python.

e=Employee() # creating an object of the class Employee

print(e.get_salary()) # calling the method get_salary() of the object e
e2=Employee() # creating another object of the class Employee
print(e2.get_salary()) # calling the method get_salary() of the object e2
print(e.company) # accessing the class attribute company using the object e
print(e2.company) # accessing the class attribute company using the object e2