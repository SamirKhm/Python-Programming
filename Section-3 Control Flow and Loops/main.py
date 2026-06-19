age = 18
if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You just became an adult!")
else:
    print("You are an adult.")

status = 404
match status:
    case 200:
        print("Success!")
    case 404:
        print("Not Found")
    case _:
        print("Unknown Status")


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for i in range(5):
    print(i) # Output: 0, 1, 2, 3, 4

count = 0
while count < 5:
    print(count)
    count += 1

for i in range(10):
    if i == 5:
        break
    print(i) # Output: 0, 1, 2, 3, 4

for i in range(5):
    if i == 2:
        continue
    print(i) # Output: 0, 1, 3, 4

for i in range(5):
    if i == 3:
        pass # Do nothing
    print(i) # Output: 0, 1, 2, 3, 4