name="harrypotter"

print(name)

#indexing
print(name[0])
print(name[1])
print(name[-1])

#slicing
print(name[0:3]) # 0 to 3-1
print(name[0:4]) # 0 to 4-1
print(name[2:-1]) # same as name[2:4] or 2 to -1-1
print(name[0:]) # 0 to end
print(name[:]) # start to end

# slicing with skipping character 
print(name[0:5:1]) # 0 to 5-1 with step 1
print(name[0:5:2]) # 0 to 5-1 with step 2


# string formatting
age=20
print("My name is " + name + " and I am " + str(age) + " years old.") # concatenation
print("My name is {} and I am {} years old.".format(name, age)) #
print(f"My name is {name} and I am {age} years old.") # f-string

# string functions
# strings are immutable in python, which means we cannot change the original string, but we can create a new string with the desired changes.

text="   Hello World   "
print(text)
print(len(text)) # length of the string
print(text.strip()) # removes leading and trailing whitespace
print(text.lstrip()) # removes leading whitespace
print(text.rstrip()) # removes trailing whitespace
print(text.upper()) # converts to uppercase
print(text.lower()) # converts to lowercase
print(text.replace("Hello", "Hi")) # replaces "Hello" with "Hi"
print(text.split()) # splits the string into a list of words
print(text.split("o")) # splits the string at each "o"
print(text.find("World")) # returns the index of the first occurrence of "World"
print(text.find("Python")) # returns -1 if "Python" is not found
print(text.count("o")) # counts the number of occurrences of "o"
print(text.startswith("   Hello")) # checks if the string starts with "   Hello"
print(text.endswith("   ")) # checks if the string ends with "   "
print(text.isalpha()) # checks if all characters are alphabetic
print(text.isdigit()) # checks if all characters are digits 
print(text.isalnum()) # checks if all characters are alphanumeric

text="Apple, Banana, Cherry"
print(text.split(", ")) # splits the string at each ", " and returns a list of fruits

print(",".join(["Apple", "Banana", "Cherry"])) # joins the list of fruits into a string with ", " as the separator

# len , ord ,chr
print(len(name)) # length of the string
print(ord("A")) # returns the ASCII value of "A"
print(chr(65)) # returns the character corresponding to the ASCII value 65, which is "A"


