# dictionary of similary objects
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# USING  GETT() TO ACCESS VALUES
alien_0 = {'color': 'green', 'speed': 'slow'}

# print(alien_0['points'])  #COMMENT TO SUPPRESS ERROR
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
print(favorite_languages.get('phil')) # extra example

# LOOPING THROUGH ALL KEY-VALUE PAIRS
user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
 }
for key, value in user_0.items():
 print(f"\nKey: {key}")
 print(f"Value: {value}")

print("\n")
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }
for name, language in favorite_languages.items():
 print(f"{name.title()}'s favorite language is {language.title()}.")
 
print(favorite_languages.items()) #extra code

# LOOP THROUGH KEYS  OF KEY-VALUE PAIRS
for name in favorite_languages.keys():
 print(name.title())

# LOOP THROUGH VALUES OF KEY-VALUE PAIRS
for language in favorite_languages.values():
    print(language.title())

# USE BOTH LIST AND DICTIONARY
print('\n')
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
 print(f"Hi {name.title()}.")
if name in friends:
    language = favorite_languages[name].title()
    print(f"\t{name.title()}, I see you love {language}!")

# USING NOT IN 
print("\n")
if 'erin' not in favorite_languages.keys():
 print("Erin, please take our poll!")

# LOOPING THROUGH DICTIONARY IN A PARTICULAR ORDER
print(favorite_languages.keys())
print(sorted(favorite_languages.keys()))

for name in sorted(favorite_languages.keys()):
 print(f"{name.title()}, thank you for taking the poll.")

#  LOOP THROUGH ALL VALUES IN A DICTIONARY
print("\n")
print("The following languages have been mentioned:")
for language in favorite_languages.values():
 print(language.title())
 
# SELECTS UNIQUE VALUES
print()
for language in set(favorite_languages.values()):
 print(language.title())