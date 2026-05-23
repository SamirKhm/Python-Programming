class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def firstname(self):
        return self.name.split(" ")[0]
    
    @firstname.setter
    def set_firstname(self, first):
        l=self.name.split(" ")
        newname=f"{first} {l[1]}"
        self.name=newname



e=Employee("John Doe", 50000)
# e.projects=6
# print(e.projects)  # Output: 6

# print(e.firstname())  # Output: John
# e.set_firstname("Jane")
# print(e.firstname())  # Output: Jane

print(e.firstname)  # Output: John
e.set_firstname="Jane"
print(e.firstname)  # Output: Jane