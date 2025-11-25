# PASSING AN ARBITRARY NUMBER OF ARGS
# EXAMPLE 1
# def make_pizza(*toppings):
#     """Print the list of toppings that have been requested."""
#     print(toppings)

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# EXAMPLE 2
# MIXING POSITIONAL AND ARBITRARY ARGS

#====================================
#SUMMARY FROM claude.ai
# Defines a function - Creates a function called make_pizza() that takes:

# size - a required parameter for the pizza size
# *toppings - an arbitrary number of toppings (the * allows any number of additional arguments)


# Prints pizza summary - The function prints the size and lists all the toppings
# Loops through toppings - For each topping provided, it prints it with a dash/bullet point
# Calls the function twice:

# First call: 16-inch pizza with just pepperoni
# Second call: 12-inch pizza with three toppings

# Key concept: The *toppings parameter is called an arbitrary argument or variable-length argument. 
# It collects any number of arguments into a tuple, allowing you to pass 1 topping, 10 toppings, 
# or even no toppings at all. This makes the function flexible - 
# you don't need to know in advance how many toppings the user wants!
#====================================
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# # USING ARBITRARY KEYWORD ARGS
# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user."""
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info


# user_profile = build_profile('albert', 'einstein',
# location='princeton',
# field='physics')
# print(user_profile)