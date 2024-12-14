# Class Inheritance and isinstance() function

# Demonstrate the use of ininstance() to check if my_tesla is an instance of a Car and ElectricCar classes

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def display_name(self):
        return f"The Car is {self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"






class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)              # --> upar wale class ki tarah ye do variable bana lo 
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

my_tesla = ElectricCar("Tesla", "Model S", "85kWH")

print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))

# print(my_tesla.fuel_type())


# safari = Car("Tata", "Safari")
# print(safari.fuel_type())