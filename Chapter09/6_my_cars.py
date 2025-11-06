# # IMPORTING MULTIPLE CLASSE FROM A MODULE
# from car_module import Car, ElectricCar

# my_mustang = Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())

# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())

# # IMPORT AN ENTIRE MODULE
# import car_module as car

# my_mustang = car.Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())

# my_leaf = car.ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())

from car_module import *

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())