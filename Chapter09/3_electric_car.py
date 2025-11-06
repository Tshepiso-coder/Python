class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """Filling up a gas tank"""
        print("Simulates filling a gas tank!")


# ========================================================================

class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")



# ========================================================================

# CHILD CLASS/SUBCLASS
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        """Then initialize attributes specific to an electric car"""
        super().__init__(make, model, year)
        # self.battery_size = 40
        self.battery = Battery()

        

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    # OVERIDE METHODS FROM PARENT
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")


    


# CREATE INSTANCE OF CHILD CLASS/SUBCLASS
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

# DEFINIG ATTRIBUTES AND METHODS FOR CHILD CLASS
# my_leaf.describe_battery()

my_leaf.fill_gas_tank()

# INSTANCE AS ATTRIBUTE
my_leaf.battery.describe_battery()

# 
my_leaf.battery.get_range()