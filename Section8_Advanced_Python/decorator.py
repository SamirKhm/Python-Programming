# A decorator is a function that takes another function as an argument, adds some functionality to it, and returns a new function.

def decorator(func):
    def wrapper():
        print("I am about to print hello")
        func()
        print("I have executed the function")
    return wrapper


def say_hello():
    print("Hello!")

#say_hello()  # Output: Hello!
#f=decorator(say_hello)
#f()  # Output: I am about to print hello
     #         Hello!
     #         I have executed the function

# def f():
#     print("I am about to print hello")
#     print("Hello!")
#     print("I have executed the function")

@decorator
def say_hello():
    print("Hello!")

say_hello()  # Output: I am about to print hello


# decorators with arguments

def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator

@repeat(3)
def say_hello(name):    
    print(f"Hello, {name}!")

say_hello("Alice")  # Output: Hello, Alice!
'''
It replaces the original say_hello function with the wrapper function that calls the original function three times. When we call say_hello("Alice"), it will print "Hello, Alice!" three times.
def decorator(func):
    def wrapper(a):
        say_hello(a)
    return wrapper

'''