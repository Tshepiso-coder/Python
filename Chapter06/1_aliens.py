# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens:
#  print(alien)

# # Make an empty list for storing aliens.
# print()
# aliens = []
# # Make 30 green aliens.
# for alien_number in range(30):
#  new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#  aliens.append(new_alien)

# Show the first 5 aliens.
# for alien in aliens[:5]:
#  print(alien)
# print("...")
# # Show how many aliens have been created.
# print(f"Total number of aliens: {len(aliens)}")


# Make 30 green aliens.
# =======================================
# SUMMARY FROM claude.ai
# This code demonstrates working with lists of dictionaries and modifying dictionary values based on conditions. 
# Here's what it does:
# Step by step:

# Creates an empty list - Starts with an empty aliens list
# Adds 3 green aliens - The first loop creates 3 dictionaries, 
# each representing a green alien with 5 points and slow speed, and adds them to the list
# Adds 3 yellow aliens - The second loop creates 3 more dictionaries 
# for yellow aliens (also 5 points and slow speed) and adds them to the list
# Prints the original list - Shows all 6 aliens before any changes
# Upgrades each alien - The third loop goes through each alien and:

# If the alien is green: changes it to yellow, medium speed, and 10 points
# If the alien is yellow: changes it to red, fast speed, and 15 points


# Prints the modified list - Shows all aliens after the upgrades

# The output:
# First print (original):

# Key concept: This simulates a game where aliens level up - green aliens become yellow and stronger,
# yellow aliens become red and even stronger!

# =======================================
aliens = []
for alien_number in range (3):
   new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
   aliens.append(new_alien)

for alien_number in range (3):
   new_alien = {'color': 'yellow', 'points': 5, 'speed': 'slow'}
   aliens.append(new_alien)

print(aliens)


for alien in aliens:
 if alien['color'] == 'green':
    alien['color'] = 'yellow'
    alien['speed'] = 'medium'
    alien['points'] = 10
 elif alien['color'] == 'yellow':
    alien['color'] = 'red'
    alien['speed'] = 'fast'
    alien['points'] = 15

print(aliens)    
    
# # Show the first 5 aliens.
# for alien in aliens[:5]:
#  print(alien)
# print("...")