class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def display_name(self):
        return f"The Car is {self.brand} {self.model}"

# car_ka_object = Car("Toyota","Corolla")
# display_ki_value = car_ka_object.display_name()

# print(display_ki_value)



# Inheritance
# Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)              # --> upar wale class ki tarah ye do variable bana lo 
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla", "Model S", "85kWH")
print(my_tesla.model)
print(my_tesla.display_name())