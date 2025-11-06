prompt = "\nEnter your age to see if you qualify for a discount."
prompt += "\nYou can enter 'quit' to exit: "
while True:

    answer =input(prompt)

    if answer.lower() == "quit":
        break
    # CHECK IF USER SUPPLIED AN INTEGER
    try:
        answer = float(answer)
    except ValueError:
        print("\n***Please enter a number.")
        continue

    if answer < 3:
        print(" You have FREE Admission" )
    elif answer <= 12:
        print("Your ticket price is: $10")
    else:
        print("The ticket will cost you $15")
