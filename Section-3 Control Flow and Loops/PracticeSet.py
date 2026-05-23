# if else
num=int(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

age = int(input("Enter your age: "))
if age < 18:
    print("You can't vote.")
elif age == 18:
    print("You can vote for the first time!")
else:
    print("You can vote.")


num=int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")    
else:
    print("The number is odd.")

# match case
day=int(input("Enter a day of the week: "))
match day:
    case 1:
        print("It's Monday!")
    case 2:
        print("It's Tuesday!")
    case 3:
        print("It's Wednesday!")
    case 4:
        print("It's Thursday!")
    case 5:
        print("It's Friday!")
    case 6:
        print("It's Saturday!")
    case 7:
        print("It's Sunday!")
    case _:
        print("Invalid day!")

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
operation=input("Enter operation (+, -, *, /): ")
match operation:
    case "+":
        print(f"Result: {num1 + num2}")
    case "-":
        print(f"Result: {num1 - num2}")
    case "*":
        print(f"Result: {num1 * num2}")
    case "/":
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Error: Division by zero!")
    case _:
        print("Invalid operation!")


# for loop
for i in range(1, 11):
    print(i)

num=int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

sum = 0
for i in range(1, 101):
    sum += i
print(f"Sum of numbers from 1 to 100: {sum}")

for i in range(1, 5):
    for j in range(1,i+1):
        print("*",end= "")
    print()

i=1
while i <= 10:
    print(i)
    i += 1

passw="12345"
password=input("Enter the password: ")
if password == passw:
    print("Access granted!")
else:
    print("Access denied!")

i=123
sum=0
while i > 0:
    digit = i % 10
    sum = sum*10 +digit
    i= i // 10
print("Reversed number is ",sum)

for i in range(1, 11):
    if i == 7:
        break
    print(i) 

for i in range(1, 11):
    if i == 5:
        continue
    print(i)

for i in range(1, 6):
    if i == 3:
        pass
    print(i)