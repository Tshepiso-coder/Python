guest = ["John", "Bob", "Will"]
print(guest)
print(f"Hello {guest[0]} you are invited")
print(f"Hello {guest[1]} you are invited")
print(f"Hello {guest[2]} you are invited")

#REMOVE BOB AND REPLACE WITH SAM
print(f"{guest[1]} can not make it")
print(guest)
guest.pop(1)
print(guest)

guest.append("Carl")
print(guest)
guest.insert(1, "Sam")
print(guest)
print(f"The total number of the guest is {len(guest)}")
del guest[2]
print(guest)
guest.remove("Carl")
print(guest)