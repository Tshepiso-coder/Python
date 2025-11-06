# IMPORTING AN ENTIRE MODULE
# import pizza_module

# pizza_module.make_pizza(16, "pepperoni", "mushrooms")

# IMPORTING A FUNCTION FORM A MODULE
# from pizza_module import make_pizza

# make_pizza(16, "bacon", "extra cheese")

# USING as TO GIVE A FUNCTION AN ALIAS
# from pizza_module import make_pizza as mp

# mp(16, "bacon", "extra cheese")

# USING as TO GIVE A MODULE AN ALIAS
# import pizza_module as p 
# p.make_pizza(16, "bacon", "extra cheese")
from pizza_module import *
make_pizza(16, "pepperoni")
make_pizza(16, "bacon", "extra-cheese")

