#funtions
def average(a,b,c):
    return (a+b+c)/3

print(average(10,20,30))

def average(numbers):
    return sum(numbers)/len(numbers)

avg=average([10,20,30])
print(avg)


# arguments and parameters

#positional arguments
def greet(name,age):
    print(f"Hello {name}, you are {age} years old.")

# default arguments
def greet(name,age=30):
    print(f"Hello {name}, you are {age} years old.")

greet("Alice",25) # positional argument
greet("Bob") # default argument

# keyword arguments
def greet(name,age):
    print(f"Hello {name}, you are {age} years old.")
greet(age=25,name="Alice") # keyword arguments


# lambda functions
square = lambda x: x**2
print(square(5))

# recursive functions

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))

def fibonacci(n):
    #base cases
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
print(fibonacci(10))



# local and global variables
x=10 # global variable

def my_function():
    x=5 # local variable
    print("Inside function:",x)

my_function()
print("Outside function:",x)

# global keyword
x=10
def my_function():
    global x # use the global variable x
    x=5
    print("Inside function:",x)

my_function()
print("Outside function:",x)


# docstrings

def greet(name):
    """This function greets the person with the given name."""
    return f"Hello {name}!"

print(greet.__doc__)
print(greet("Alice"))