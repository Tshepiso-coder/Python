#NUMERICAL LISTS
#USING RANGE() FUNCTIONS

for value in range(1, 5):
    print(value)

#USING RANGE() TO MAKE LIST OF NUMBERS
numbers = list(range(1, 6)) #list is an int
print(type)
print(numbers)

print("\n")
even_numbers = list(range(2, 11, 2))
print(even_numbers)

#SQUARES
squares = []
for value in range(1, 11): 
    square = value ** 2
    squares.append(square)
print(squares)

#squares = list(value ** 2 for value in range(1,11))
squares = list(value ** 2 for value in range(1,11))
print(f"Squares: {squares}")

# squares = []
# for value in range(1, 11): 
#     square = value ** 2
#     squares.append(square)
# print(squares)

#SIMPLE STATS WITH NUMBERS
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(sorted(digits))
print(f"Min = {min(digits)}")
print(f"Max = {max(digits)}")
print(f"Sum = {sum(digits)}")

print("\n")

# Squares = list(value ** 2 for value in range(1, 11))
squares = [value **2 for value in range(1, 11)]
print(squares)
