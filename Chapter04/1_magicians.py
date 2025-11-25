
#LOOPING THROUGH ENTIRE LIST
# ====================
# This code works with a list and demonstrates Python's **for loop** functionality. Here's what happens:

# **What the code does:**

# 1. **Creates a list of magicians** - Stores three names: 'alice', 'david', and 'carolina'

# 2. **Loops through each magician** - The for loop processes each name in the list, one at a time

# 3. **Prints messages for each magician** - For every magician, it prints:
#    - A compliment about their trick (with their name capitalized using `.title()`)
#    - A message expressing excitement for their next trick

# 4. **Prints a final thank you message** - After all magicians have been processed, it prints a closing message to everyone

# The main concept illustrated is that indented code runs for each list item, while non-indented code after the loop runs only once.


# ====================

magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!!")
    print(f"I can't wait to see your next trick, {magician.title()}.")

print("\nThank you, everyone. That was a great magic show!")




# #AVOIDING INDENTATION ERRORS
# #NOTE: RESULTS IN INDETATION ERROR
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician)   

# #Indenting Unnecessarily

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
#     print(f"I can't wait to see your next trick, {magician.title()}.\n")

# #Forgetting the Colon