# while True:
#     try:
#         a=int(input("Enter a number: "))
#         b=int(input("Enter another number: "))

#         print("The sum is: ", a+b)
    
#     except Exception as e:
#         print("Please enter a valid number.")
#         print("Error details: ", e)


a=int(input("Enter a number: "))
b=int(input("Enter another number: "))

if b==0:
    raise ValueError("Cannot divide by zero.")

print("The division is: ", a/b)
