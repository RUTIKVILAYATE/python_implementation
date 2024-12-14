# class variables

# Add a class variable to Car that keeps track of the number of cars created


class Car:
    total_cars = 0

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        Car.total_cars += 1   # No. of cars increases by 1

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

print(my_tesla.fuel_type())


safari = Car("Tata", "Safari")
safari_three = Car("Tata", "Nexon")
# print(safari.fuel_type())

print(Car.total_cars)       # --> no. of objects == no. of cars  --> by defining attribute total_cars in __init__ method and access by class_name.total_cars