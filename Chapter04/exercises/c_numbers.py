
# #NUMBER 1 TO 20 INCLUSIVE
# for value in range(1,21):
#     print(value)

# for value in range(1, 1_000_001):
#     print(value)
numbers =[value for value in range(1, 1_000_001)]  
print(min(numbers))
print(max(numbers))
print(sum(numbers))

odd_numbers = list(value for value in range(1,21,2))
print(odd_numbers)

threes = list(value for value in range(3,31,3))
for value in threes:
    print(value)

cubes = list(value **3 for value in range(1,11))

for value in cubes:
    print(value)   

print(cubes)