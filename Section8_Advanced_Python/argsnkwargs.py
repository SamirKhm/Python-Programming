def sum(a,b):
    return a+b

print(sum(1,2))
# print(sum(3,4,5)) # this will raise an error because the function only accepts 2 arguments

def sum(*args):
    print(args) # this will print the tuple of arguments passed to the function
    total = 0
    for num in args:
        total += num
    return total

print(sum(1,2,3,4,5))

# kwargs - keyword arguments

def marks(**kwargs):
    for i in kwargs.keys():
        print(kwargs[i])


marks(english=90, math=95, science=85)

# combined - args and kwargs

def func1(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

func1(1,2,3, name="Alice", age=30)
