# Define the Car class
class Car:
    # The constructor method to initialize the object
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Method to return a description of the car
    def describe(self):
        return f"This car is a {self.year} {self.make} {self.model}."

# Create instances of the Car class
my_car = Car("Toyota", "Corolla", 2020)
car1 = Car("Honda", "Civic", 2019)
car2 = Car("Ford", "Mustang", 2022)
car3 = Car("Tesla", "Model 3", 2021)

# Print the description of all cars
print(my_car.describe())
print(car1.describe())
print(car2.describe())
print(car3.describe())