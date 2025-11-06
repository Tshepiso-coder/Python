# This Python code:
# Creates a nested dictionary named users, where each key is a username ('aeinstein', 'mcurie'), and each value is another dictionary containing:
# 'first' name
# 'last' name
# 'location'
# Iterates through each user using a for loop.
# Prints formatted user information, including:
# Username
# Full name (with proper capitalization using .title())
# Location (also title-cased


users = {
 'aeinstein': {
 'first': 'albert',
 'last': 'einstein',
 'location': 'princeton',
 },
 'mcurie': {
 'first': 'marie',
 'last': 'curie',
 'location': 'paris',
 },
 }

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")