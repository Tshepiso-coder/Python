#============================
#SUMMARY FROM claude.ai

# Defines a Dog class - Creates a template for dog objects with:

# __init__ method: Constructor that sets up each dog with a name (automatically capitalized) and age
# sit() method: Simulates the dog sitting
# roll_over() method: Simulates the dog rolling over

# Creates first dog instance (my_dog) - Instantiates a dog named "Milo" (age 3)
# Accesses attributes - Retrieves and prints Milo's name and age using dot notation (my_dog.name, my_dog.age)
# Calls methods - Executes the sit() and roll_over() methods on Milo
# Creates second dog instance (your_dog) - Instantiates another dog named "Khuphar" (age 3)
# Uses second instance - Prints Khuphar's details and calls the sit() method

#============================
# CREATING A DOG CLASS
class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialise name and age attributes"""
        self.name = name.title()
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
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

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()