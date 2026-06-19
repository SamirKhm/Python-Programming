# walnus operator

def very_slow_func():
    print("Calculating...")
    return 42

#a=very_slow_func() # this will call the function and store the result in a variable
if((a:=very_slow_func()) > 40):
    print(a)
else:    
    print("The answer is 40 or less")

while(data:= input("Enter some data (or 'exit' to quit): ") != 'exit'):
    print(f"You entered: {data}")
    if data == 'exit':
        break