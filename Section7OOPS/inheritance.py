class Animal: # Parent class (superclass)

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Generic animal sound")


class Dog(Animal): # Dog inherits from Animal (Dog is a subclass of Animal)
    def speak(self): # We *override* the speak method (more on this later)
        super().speak() # Call the speak method of the parent class (Animal)
        print("Woof!")


class Cat(Animal): # Cat also inherits from Animal
    def speak(self):
        print("Meow!")

a=Animal("Generic Animal")
a.speak() # Output: Generic animal sound

d=Dog("Buddy")
d.speak() # Output: Woof!

c=Cat("Whiskers")
c.speak() # Output: Meow!