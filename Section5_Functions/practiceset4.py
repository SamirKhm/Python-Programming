# defining func

def greet(name):
    print(f"Hello, {name}!")

def square(x):
    return x**2

print(greet("Alice"))
print(square(5))

# function arguments and parameters

def full_name(first,last):
    return f"{first} {last}"

print(full_name("Alice", "Smith"))

def area(l,w=10):
    return l*w
print(area(5))
print(area(5,20))

# lamda functions

add=lambda x,y:x+y
print(add(5,10))

l=[1,2,3,4,5]

numbers = [1,2,3,4,5]

squares = list(map(lambda x: x*x, numbers))

print(squares)

# recursive functions

def sum_of_digits(n):
    if n==0:
        return 0
    else:
        return n%10 + sum_of_digits(n//10)
    
print(sum_of_digits(12345))

# n//10 is integer division, which removes the last digit of n. n%10 gives the last digit of n. The function calls itself with the remaining digits until n becomes 0, at which point it returns 0 and the recursion ends.

# n//10 means integer division, which divides n by 10 and discards the decimal part. For example, if n is 12345, n//10 will give 1234. This effectively removes the last digit of n.


# modules

import math
print(math.sqrt(16))

print(math.sin(math.radians(90)))

import requests

a=requests.get("https://api.github.com/")
print(a.json())


