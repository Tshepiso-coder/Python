prompt = "\nEnter the toppings for your pizza." 
prompt += "\nPlease enter quit when done. "

toppings = ""

while toppings.lower() != "quit":
    toppings = input(prompt)
    if toppings != "quit":
        print(f"The {toppings.upper()} topping has been added to your pizza")
