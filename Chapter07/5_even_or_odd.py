#=======================
# SUMMARY FROM claude.ai

# Gets user input - Prompts the user to enter a number using input(), which returns the input as a string
# Converts to integer - Converts the string input to an integer using int() so mathematical operations can be performed
# Checks if even or odd - Uses the modulo operator % to check divisibility:

# number % 2 == 0 checks if the remainder when dividing by 2 is zero
# If the remainder is 0, the number is even
# Otherwise, the number is odd


# Prints the result - Displays a message telling the user whether their number is even or odd

# Key concept: The modulo operator % returns the remainder of division. 
# Any number divisible by 2 (with no remainder) is even, while numbers with a remainder of 1 when divided by 2 are odd.

#=======================

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
 print(f"\nThe number {number} is even.")
else:
 print(f"\nThe number {number} is odd.")