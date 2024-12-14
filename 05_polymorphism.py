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

print(my_tesla.fuel_type())


safari = Car("Tata", "Safari")
print(safari.fuel_type())

