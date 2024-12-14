# Static Method

# Add a static method to the Car class that returns a general description of a car

# static() --> method belongs to the class rather that instance of the class


class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def display_name(self):
        return f"The Car is {self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod       # if want to access method after it --> the method should be called by class directly without parameter self
    def general_description():
        return "Cars are means of transport"


my_car = Car("Tata", "Safari")


# print(my_car.general_description())

print(Car.general_description())

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)              # --> upar wale class ki tarah ye do variable bana lo 
#         self.battery_size = battery_size

#     def fuel_type(self):
#         return "Electric Charge"

# my_tesla = ElectricCar("Tesla", "Model S", "85kWH")

# print(my_tesla.fuel_type())


# safari = Car("Tata", "Safari")
# print(safari.fuel_type())