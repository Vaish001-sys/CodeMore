# animals.py
# This file demonstrates inheritance and polymorphism using Animal classes.

# ----------------------------
# Base Class
# ----------------------------

class Animal:
    """
    A base class to represent a generic animal.

    Attributes:
        name (str): The name of the animal.
    """

    def __init__(self, name):
        """
        Initialize the Animal with a name.

        Args:
            name (str): The name of the animal.
        """
        self.name = name

    def speak(self):
        """
        Make the animal speak.
        This method is meant to be overridden by child classes.
        """
        print(f"{self.name} makes a sound.")


# ----------------------------
# Child Class: Dog
# ----------------------------

class Dog(Animal):
    """
    A class to represent a Dog. Inherits from Animal.
    """

    def speak(self):
        """Override speak() to make the Dog bark."""
        print(f"{self.name} says: Woof! Woof!")


# ----------------------------
# Child Class: Cat
# ----------------------------

class Cat(Animal):
    """
    A class to represent a Cat. Inherits from Animal.
    """

    def speak(self):
        """Override speak() to make the Cat meow."""
        print(f"{self.name} says: Meow! Meow!")


# ----------------------------
# Create objects
# ----------------------------

dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call speak() on each object individually
print("---- Individual Animal Sounds ----")
dog.speak()
cat.speak()

# ----------------------------
# Demonstrate Polymorphism
# ----------------------------
# Polymorphism: same method name (speak) behaves differently
# depending on which class the object belongs to.

print("\n---- Polymorphism Demo ----")

# Store different animal objects in a list
animals = [Dog("Rex"), Cat("Luna"), Dog("Max"), Cat("Bella")]

# Loop through each animal and call speak()
# Python automatically uses the correct speak() for each object
for animal in animals:
    animal.speak()
