
#Tuple

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

dimensions[0] = 250
print("\n")

for dimension in dimensions:
    print(dimension)

dimensions = (400, 100) #overwriting tuple
for dimension in dimensions:
    print(dimension)