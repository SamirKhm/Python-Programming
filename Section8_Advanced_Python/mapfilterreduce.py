# map - applies a function to each item in a list

number=[1,2,3,4,5,6]

def square(x):
    return x**2

new=map(square,number)
print(list(new))

# filter - filters items in a list based on a condition

def is_greater_than_3(x):
    if x>3:
        return True
    else:        
        return False

a=[1,2,3,45,67,789]

new=filter(is_greater_than_3,a)
print(list(new))

# reduce - applies a function to the items in a list and reduces it to a single value

from functools import reduce
def add(x, y):
    return x + y

a=[1,2,3,4,5]
new=reduce(add,a)
print(new)
