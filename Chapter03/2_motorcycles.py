# MODIFYING ELEMENT IN A LIST
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = "ducati"
print(motorcycles)

print("\n")
# APPENDING AN ELEMENT TO END OF LIST (It's like push)
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.append("ducati")
print(motorcycles)

print("\n")
motorcycles = []
print(motorcycles)
motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")
print(motorcycles)

print("\n")
# INSERTING ELEMENTS INTO A LIST
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, "ducati")
print(motorcycles)

print("\n")

# REMOVING AN ITEM USING DEL STATEMENT
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[1] #To remove it using the position
print(motorcycles)

print("\n")

# REMOVING AN ITEM USING POP() METHOD
motorcycles = ['honda', 'yamaha', 'suzuki']

popped_motorcycle = motorcycles.pop()
print(f"Popped Motorcycle = {popped_motorcycle}\nNew List = {motorcycles}")

print("\n")

# POPPING ITEMS FROM ANY POSITION IN THE LIST
motorcycles = ['honda', 'yamaha', 'suzuki']

second_owned = motorcycles.pop(1)
print(f"The second motorcycle I owned was a {second_owned.title()}")

print("\n")
# REMOVING AN ITEM BY VALUE
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.remove('honda')
print(motorcycles)

motorcycles.append("ducati")
print(motorcycles)

too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(f"A {too_expensive.title()} is too expensive for me.\nMy current wish list is now: {motorcycles}")





