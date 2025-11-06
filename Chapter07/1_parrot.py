prompt = "\nTell me something and I will speak it back to you"
prompt  += "\nEnter 'quit' to end the program. "

message  = ""

# while message.lower() != "quit":
#     message = input (prompt)
#     print(message)

#WHILE USING A FLAG
active = True

while active:
 message = input(prompt)
 if message == 'quit':
    active = False
 else:
    print(message)