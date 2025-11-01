
# #SIMPLE IF STATEMENT EXAMPLE

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#Checking for Equality
car = 'bmw'
print(f"Car - {car}")
print(f"Is the car a bmw?:{car == "bmw"}")

print("\n")
car = 'audi'
print(f"Car - {car}")
print(f"Is the car a audi?:{car == "audi"}")
print(f"\nIs the car a audi?: {car.lower() == "audi"}")

#Checking for Inequality
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("\nHold the anchovies!")