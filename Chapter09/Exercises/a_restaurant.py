class Restaurant:
    """a class that models different resturant type"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    # METHODS
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} food !")
    
    def open_restaurant(self):
        """Indicates that restaurant is now open"""
        print(f"{self.restaurant_name} is now open for business!")

# INSTANTIATE INSTANCES OF CLASS
restaurant_1 = Restaurant("Chicken Licken","Chicken")

print(f"--- ACCESSING ATTRIBUTES ---")
print(f"The restuarant name is : {restaurant_1.restaurant_name}")
print(f"They serve: {restaurant_1.cuisine_type}")


print("\n--- METHOD CALLS ---")
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

# ================================================
# ================================================

# 9.3 THREE RESTAURANTS
restaurant_2 = Restaurant("Mikes Kitchen", "Italian" )
