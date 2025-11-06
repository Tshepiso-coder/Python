# DEFINING A SIPLE FUNCTION
def greet_user():
    """
    Display a simple greeting.
   *** Multi line comment***
    """
    print("Hello!")


greet_user()


# PASSING INFO TO A FUNCTION
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('VUSI')
