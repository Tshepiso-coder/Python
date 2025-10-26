cities = ["london", "paris", "new york", "helsinki", "Rio"]
print(cities)
print(sorted(cities)) # keeps the original order of the list
print(cities)

cities.reverse()
print(cities)

cities.sort() # actual changes the order of the original list
print(cities)
print(cities[-4])
cities.sort() 