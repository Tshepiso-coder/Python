#LOOPING THROUGH ENTIRE LIST
magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(f"{magician.title()},that was a great trick!!")
    print(f"I can't wait to see your next trick, {magician.title()}.")

print("Thank you, everyone. That was a great magic show!\n")
print("\n")

#AVOIDING INDENTATION ERRORS
#NOTE: RESULTS IN INDETATION ERROR
#magicians = ['alice', 'david', 'carolina']
#for magician in magicians:
#print(magician)

#Indenting Unnecessarily

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
#     print(f"I can't wait to see your next trick, {magician.title()}.\n")

#Forgetting the Colon