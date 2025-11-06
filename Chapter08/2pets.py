# PASSING ARGUMENTS

# 1) POSITIONAL ARGUMENTS
# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")


# describe_pet('dog', 'milo')
# describe_pet('cat', 'khuphar')

# 1)KEYWORD ARGUMENTS
# describe_pet(animal_type='hamster', pet_name='harry')
# describe_pet(pet_name='harry',animal_type='hamster')

# # FUNCTION WITH DEFAULT VALUE
# # parameter with a default value comes at the end of the parament list
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet(pet_name='khuphar')
# describe_pet("milo")
# # overrides the default value
# describe_pet("khuphar","cat")
# describe_pet(animal_type='hamster', pet_name='harry') 

# # EQUIVALENT FUNCTION CALLS
# # A dog named Willie.
# describe_pet('willie')
# describe_pet(pet_name='willie')




# # A hamster named Harry.
describe_pet(animal_type='hamster',pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet("harry")