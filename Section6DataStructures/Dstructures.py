# Lists in Python

numbers = [1, 2, 3, 4, 5]
mixed = [10, "hello", 3.14]
my_list = [1, 2, 3]
print(my_list[0]) # Output: 1
print(my_list[1]) # Output: 2


my_list.append(4) # [1, 2, 3, 4]
print(my_list) # Output: [1, 2, 3, 4]

my_list.insert(1, 99) # [1, 99, 2, 3, 4]
print(my_list) # Output: [1, 99, 2, 3, 4]

my_list.remove(2) # [1, 99, 3, 4]
print(my_list)

my_list.pop() # Removes last element -> [1, 99, 3]
print(my_list)

my_list.reverse() # [3, 99, 1]
print(my_list)

my_list.sort() # [1, 3, 99]
print(my_list)

print(len(my_list)) # Output: 3
print(99 in my_list) # Output: True
print(100 in my_list) # Output: False
print(my_list[:])

list1 = [1, 2, 3]

my_list.extend(list1) # [1, 3, 99, 1, 2, 3]
print(my_list)  


# list comprehension

# create a list containing table of 5

a=5
table=[]
for i in range(1, 11):
    table.append(a * i)

print(table) # Output: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

table_of_5 = [5 * i for i in range(1, 11)]
print(table_of_5) # Output: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]


# Tuples in Python

my_tuple = (1, 2, 3)
print(my_tuple[0]) # Output: 1

print(my_tuple.count(2)) # Output: 1
print(my_tuple.index(3)) # Output: 2

a,b,c=my_tuple
print(a) # Output: 1


# sets in Python

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.add(6)) # Output: None
print(set1) # Output: {1, 2, 3, 6}
set1.add(6)
print(set1.remove(6)) # Output: None

print(set1) # Output: {1, 2, 3, 4, 5}

print(type(set1)) # Output: <class 'set'>

set1.remove(3)


# Dictionaries in Python

dict1 = {"name": "Alice", "age": 30, "city": "New York"}
print(dict1["name"]) # Output: Alice
dict1["age"] = 31
print(dict1) # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'}

dict1.popitem() # Removes last item
print(dict1) # Output: {'name': 'Alice', 'age': 31}

dict1.update({"country": "USA"})
print(dict1) # Output: {'name': 'Alice', 'age': 31, 'country': 'USA'}

dict1.keys() # Output: dict_keys(['name', 'age', 'country'])
dict1.values() # Output: dict_values(['Alice', 31, 'USA'])
dict1.items() # Output: dict_items([('name', 'Alice'), ('age',