# RETURNING A DICTIONARY
# EXAMPLE 1
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name.title(), 'last': last_name.title()}
    
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

# EXAMPLE 2
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age

    return person


musician = build_person('jimi', 'hendrix', age=27)
print(musician)

musician = build_person('jimi', 'hendrix')
print(musician)

musician = build_person('jimi', 'hendrix', 27)
print(musician)