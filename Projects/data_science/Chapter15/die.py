from random import randint

# =========================================================================
# SUMMARY OF class Die FROM clause.ai
# This code defines a Die class that simulates a dice roll.
# The class creates a die with a customizable number of sides (defaulting to 6 for a standard die). 
# It has a roll() method that returns a random integer between 1 and the number of sides, inclusive.
# This allows you to create dice of any size (6-sided, 20-sided, etc.) and roll them to get random results.
# =========================================================================
class Die:
    """A class representing a single die."""
    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides
    def roll(self):
        """"Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)