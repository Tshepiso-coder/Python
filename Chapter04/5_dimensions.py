
# Tuple

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# ERROR IMMUTABLE: TypeError: 'tuple' object does not support item assignment
dimensions[0] = 250
print("\n")

for dimension in dimensions:
    print(dimension)

# CAN REASSIGN THE ENTIRE TUPLE
dimensions = (400, 100) #overwriting tuple
for dimension in dimensions:
    print(dimension)