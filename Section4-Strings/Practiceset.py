# basic opeations on string

name="Alice"
print(name[0])
print(name[-1])
print(len(name))

str1='hello'
str2="world"

print(str1+" "+str2) # concatenation

# slicing and indexing

text="Python Programming"
print(text[0:6]) # slicing from index 0 to 5
print(text[-6:]) # slicing from index -6 to the end
print(text[::2])

print(text[::-1]) # reverse the string

# methods of string

s=" i love python prograamming"

print(s.strip()) # removes leading and trailing whitespace
print(s.title()) # converts to title case
print(s.count("o")) # counts the number of occurrences of "o"

s1="123abc"
print(s1.isalnum()) # checks if all characters are alphanumeric

# formatting strings

name="John"
age=25
print("My name is " + name + " and I am " + str(age) + " years old.") # concatenation
print("My name is {} and I am {} years old.".format(name, age)) # using format method
print(f"My name is {name} and I am {age} years old.") # using

# string manipulation

sentence="Coding in Python is fun"
print(sentence.replace("fun","awesome"))
print(sentence.find("Python"))
print(sentence.upper())

#Write a program that counts how many vowels are in a given string.

string="Hello World"

vowels="aeiouAEIOU"
count=0
for char in string:
    if char in vowels:
        count+=1

print("Number of vowels in the string:", count)

# Take a user input string and check if it is a palindrome (same forwards and
#backwards).

user_input=input("Enter a string: ")
if user_input==user_input[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")