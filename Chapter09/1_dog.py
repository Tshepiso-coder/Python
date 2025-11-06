# CREATING A DOG CLASS
class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialise name and age attributes"""
        self.name = name.title()
        self.age = age

    def sit(self):
        """simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(F"{self.name} rolled over!")

# CREATE AN INSTANCE OF THE CLASS (INSTANTIATE)
my_dog = Dog("milo", 3)

# ACCESSING THE CLASS ATTRIBUTES
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# CALLING THE CLASS METHODS
my_dog.sit()
my_dog.roll_over()

# CREATING MULTIPLE INSTANCES
your_dog = Dog('khuphar', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()