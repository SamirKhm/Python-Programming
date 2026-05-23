# list

fruits=["apple","banana","cherry"]

print(fruits[0]) # Output: apple
fruits[1]="orange"
print(fruits) # Output: ['apple', 'orange', 'cherry']
print(len(fruits)) # Output: 3

num=[1,2,3,4,5,6,7,8,9,10]

print(num[0:3])
print(num[-3:])

# list methods

num=[5,2,9,1,7]

num.sort() # [1, 2, 5, 7, 9]
print(num)

num.append(10)
print(num) # [1, 2, 5, 7, 9, 10]

num.remove(2)
print(num) # [1, 5, 7, 9, 10]

names=["Alice", "Bob", "Charlie"]
names.insert(1, "David")
print(names) # ['Alice', 'David', 'Bob', 'Charlie']


# Tuples    

cordinates=(10,20)
print(cordinates[0]) # Output: 10
print(cordinates[1]) # Output: 20

#cordinates[0]=30 # This will raise an error because tuples are immutable

x=list(cordinates) # Convert tuple to list
x[0]=30
cordinates=tuple(x) # Convert back to tuple
print(cordinates) # Output: (30, 20)

# Set
my_set={1,2,3,4,5,5}
print(my_set)

my_set.add(5)
my_set.remove(2)
print(my_set) # Output: {1, 3, 4, 5}
print(4 in my_set) # Output: True


# Dictionary

student={"name":"John","age":20,"grade":"A"}

print(student["name"]) # Output: John
student["grade"]="A+"
print(student) # Output: {'name': 'John', 'age': 20, 'grade': 'A+'}
student["city"]="Delhi"
print(student) # Output: {'name': 'John', 'age': 20, 'grade': 'A+', 'city': 'Delhi'}

# write a program that takes a list of numbers and removes all duplicates using a set

num=[1,2,3,3,4,4,5,6,7,7]

unique_num=set(num)
unique_num=list(unique_num)
print(unique_num) # Output: [1, 2, 3, 4,

# write a program that merges two dictionaries


dict1={"name":"Alice","age":30,"city":"New York"}
dict2={"name":"Bob","age":25,"city":"Los Angeles"}
merged_dict={**dict1,**dict2}
print(merged_dict) # Output: {'name': 'Bob', 'age': 25